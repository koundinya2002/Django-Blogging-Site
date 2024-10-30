from django.urls import path
from . import views
from .views import ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, LikeView, LikeArticleView, commenting, responses # HomeView,

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:pk>',ArticleDetailView.as_view(), name = "article-detail"),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name = "update_post"),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('like/<int:pk>', LikeView, name = 'like_post'),
    path('like_article/<int:pk>', LikeArticleView, name = 'like_article_post'),
    path('article/add_comment/<int:pk>', commenting.as_view(), name="comments" ),
    path('article/add_reply/<int:pk>', responses.as_view(), name="responses"),
]