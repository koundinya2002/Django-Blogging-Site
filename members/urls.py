from django.urls import path
from.views import UserRegistrationView, UserEditView
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('user_guidelines/', views.user_guidelines, name='user_guidelines'),
]
