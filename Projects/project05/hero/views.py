from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Superhero


def allheros(request):
        heros = Superhero.objects.all()
        contex = {'heros':heros}
        return render(request, 'hero.html', contex)

#class HeroView(TemplateView):
    #template_name = "hero.html"

class BasePage(TemplateView):
    template_name = "superhero_theme.html"

class AboutPage(TemplateView):
    template_name = 'about.html'

class HomePage(TemplateView):
    template_name = 'home.html'

class ProfilePage(TemplateView):
    template_name = 'profile.html'

