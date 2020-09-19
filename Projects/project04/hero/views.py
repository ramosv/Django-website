from django.shortcuts import render
from django.views.generic import TemplateView


class HeroView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        id = kwargs.get('identity', 'hulk')
        return {'hero': id, 'css': '/static/hero.css'}

class BasePage(TemplateView):
    template_name = "superhero_theme.html"

class AboutPage(TemplateView):
    template_name = 'about.html'

class HomePage(TemplateView):
    template_name = 'home.html'

class ProfilePage(TemplateView):
    template_name = 'profile.html'

    
    
