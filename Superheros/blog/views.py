from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Postblog


class BlogListView(ListView):
    model = Postblog
    template_name = 'blog.html'

class BlogDetailView(DetailView):
    template_name = 'blog_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Postblog, id=id_)

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Postblog
    template_name = 'blog_add.html'
    fields = ['title', 'text', 'hero']

    def form_valid(self, form):
        form.instance.author_id = self.request.user.pk
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Postblog
    template_name = 'blog_edit.html'
    fields = ['title', 'text']

class BlogDeleteView(LoginRequiredMixin, DeleteView): 
    model = Postblog
    template_name = 'blog_delete.html'

class BasePage(TemplateView):
    template_name = "superhero_theme.html"

class AboutPage(TemplateView):
    template_name = 'about.html'

class HomePage(TemplateView):
    template_name = 'home.html'

class ProfilePage(TemplateView):
    template_name = 'profile.html'
