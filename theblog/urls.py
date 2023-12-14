from django.urls import path, include
#from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, LikeView

urlpatterns = [
    #path('', views.home, name='home')
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>',ArticleDetailView.as_view(), name = "article-detail"),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    # path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name = "update_post"),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    # path('category/<str:cat>', CategoryView.as_view(), name='category'),
    path('like/<int:pk>', LikeView, name = 'like_post'),
    # path('dislike/<int:pk>', DisLikeView, name = 'dislike_post'),
]