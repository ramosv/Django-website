from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = 'page.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'My About Page', 
            'body': 'some text',
        }
    
    
class HeroView(TemplateView):
    template_name = "page.html"
    def get_context_data(self, **kwargs):
        return {
            'title': 'My Home Page', 
            'body': 'Use these links to view my favorite Heros',
        }
    
    
class ProfileView(TemplateView):
    template_name = "page.html"
    
    def get_context_data(self, **kwargs):
        return {
            'title': 'My Profile Page', 
            'body': 'some text',
        }

class HomeView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        return {
            'title': 'My Home Page', 
            'body': 'some text',
        }