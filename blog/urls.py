from django.urls import path
from . import views

# all page url function path here fo this blog project
urlpatterns = [
    path('', views.home, name='index'),
    path('post/<int:pk>/', views.single_post_view, name='single_post_view'),
    path('register/',views.register_view,name='register_url_view'),
    path('login/',views.login_view,name='login_url_view'),
    path('dashboard/',views.dashboard_view,name='dashboard_url_view'),
    path('catagory/',views.category_view,name='category_url'),
    path('about/',views.about_view,name='about_view_url'),
    path('author/',views.author_view,name='author_view_url'),
    path('404/',views.erre_404_view,name='erre_404_view_url'),
    path('contact/',views.contact_view,name='contact_view_url'),
    
]