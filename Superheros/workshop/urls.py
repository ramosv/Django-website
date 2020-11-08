from django.contrib import admin
from django.urls import path

from .views import CardsView, HomeView


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('workshop/', HomeView.as_view(), name='workshop'),
    path('workshop/cards',  CardsView.as_view(), name='cards'),

]