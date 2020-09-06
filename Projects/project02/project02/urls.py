from django.urls import path

from page.views import AboutView, HeroView, ProfileView, HomeView
from hero.views import HulkView, WidowView, IronView, SpiderView


urlpatterns = [
    path('about', AboutView.as_view()),
    path('home', HomeView.as_view()),
    path('hero', HeroView.as_view()),
    path('profile', ProfileView.as_view()),
    path('hulk', HulkView.as_view()),
    path('black_widow', WidowView.as_view()),
    path('ironman', IronView.as_view()),
    path('spiderman', SpiderView.as_view()),
    path('', HeroView.as_view()),
]