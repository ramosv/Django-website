from django.db import models
from django.urls import reverse
#from hero.models import Superhero


class Postblog(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(null=True, max_length=200)
    text = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.author} - {self.title}'
    
#    def get_absolute_url(self): 
#        return reverse('blog_detail', args=[str(self.id)])
