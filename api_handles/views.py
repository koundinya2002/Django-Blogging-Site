from django.shortcuts import render
from .serializers import PostSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
import requests
from django.contrib.auth.decorators import login_required
from theblog.models import Post
from django.contrib.auth.models import User, Group
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# loggin-in
@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def test_token(request):
    return Response("passed for {}".format(request.user.email))


# home view
@api_view(['GET', 'POST'])
def api_home(request):
    if request.method == 'GET':
        blogs = Post.objects.all()
        # blogs = tuple(reversed(blogs))
        users_in_group = User.objects.filter(groups__name="verification")
        devs = User.objects.filter(groups__name="developers")
        blog_serializer = PostSerializer(blogs, many=True)
        user_serializer = UserSerializer(users_in_group, many=True)
        dev_serializer = UserSerializer(devs, many=True)
        return Response({
            "files": blog_serializer.data,
            "verified": user_serializer.data,
            "developers": dev_serializer.data,
            "comments": comment_serializer.data,
            "reply": reply_serializer.data,
        })        
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# blog-details view
@api_view(['GET', 'PUT', 'DELETE'])
def api_details(request, pk):
    blog = Post.objects.get(id=pk)
    if request.method == 'GET':
        serializer = PostSerializer(blog)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)