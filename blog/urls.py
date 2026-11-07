from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('post/<int:pk>/', views.single_post_view, name='single_post_view'),
    path('register/', views.register_view, name='register'),
]