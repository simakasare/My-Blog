from django.contrib import admin
from . models import Blog
from . models import User

admin.site.register(Blog)
admin.site.register(User)

# Register your models here.
