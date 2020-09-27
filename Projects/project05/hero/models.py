from django.db import models

from django.db import models

class Superhero(models.Model):
    name = models.CharField(max_length=50)
    identity = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.identity}'
    
