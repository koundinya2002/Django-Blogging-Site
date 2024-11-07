from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Reply
from .forms import PostForm, EditForm, CommentForm, ResponseForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer
import requests
from django.shortcuts import render

def LikeView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse("home"))


def LikeArticleView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse("article-detail", args=[str(pk)]))


def home(request):
    blogs = Post.objects.all()
    blogs = tuple(reversed(blogs))
    users_in_group = User.objects.filter(groups__name = "verification")
    devs = User.objects.filter(groups__name = "developers")
    # verified = User.groups.filter(groups_name="verified")
    return render(request, "home.html", {
        "files": blogs,
        "verified": users_in_group,
        "developers": devs,
    })


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'



class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class commenting(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'article_details.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy("home")

def comment_order():
    comments = Comment.objects.filter(post = Post.pk)
    comments = tuple(reversed(comments))
    return render("article-details.html",{
        "comments": comments
    })


class responses(CreateView):
    model = Reply
    form_class = ResponseForm
    template_name = 'responses.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.comment_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy("home")


# def api_home(request):    
#     return render(request, 'test.html', {'data': serializer})