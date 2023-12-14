from django.urls import path, include
from.views import UserRegistrationView, UserEditView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),

    # for the change password 'url', refer 'urls.py' of ablog.
    
]   
