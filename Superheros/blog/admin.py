from django.contrib import admin
from .models import *

admin.site.register(Postblog)
prepopulated_fields = {'slug': ('title',)}
