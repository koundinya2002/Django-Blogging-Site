from django.urls import path, include
from.views import UserRegistrationView, UserEditView, ShowProfilePageView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('user_guidelines/', views.user_guidelines, name='user_guidelines'),
    path('<int:pk>/profile', ShowProfilePageView.as_view(), name="profile_page")

    # for the change password 'url', refer 'urls.py' of ablog.

]
