from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_secret, name='create_secret'),
    path('<str:unique_url>/', views.view_secret, name='view_secret'),
]