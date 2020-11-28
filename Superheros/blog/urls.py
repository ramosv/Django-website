from .views import AboutPage, BasePage, HomePage, ProfilePage, BlogDetailView, BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView
from django.urls import path, include
from .models import Postblog
from . import views

urlpatterns = [
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog', BlogListView.as_view(), name='blog'),
    
    path('blog/new/', BlogCreateView.as_view(model=Postblog, success_url="/blog"), name='blog_add'),
    path('blog/<int:pk>/delete/', 
        BlogDeleteView.as_view(model=Postblog, success_url="/blog"), name='blog_delete'),
    path('blog/<int:pk>/edit/',
        BlogUpdateView.as_view(model=Postblog, success_url="/blog"), name='blog_edit'),
    path('about', AboutPage.as_view()),
    path('home', HomePage.as_view()),
    path('profile', ProfilePage.as_view()),
    path('', HomePage.as_view()),

] 
