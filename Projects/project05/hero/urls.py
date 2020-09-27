from .views import AboutPage, BasePage, HomePage, ProfilePage, allheros
from django.urls import path
from . import views

urlpatterns = [
    path('', HomePage.as_view()),
    path('about', AboutPage.as_view()),
    path('home', HomePage.as_view()),
    path('hero', views.allheros, name= "hero"),
    path('profile', ProfilePage.as_view()),
    path('base', BasePage.as_view()),
    #path('<str:identity>', HeroView.as_view()),
]