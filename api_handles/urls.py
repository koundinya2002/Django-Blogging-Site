from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_home, name='api_home'),
    path('<int:pk>/', views.api_details, name='api_details'),
]