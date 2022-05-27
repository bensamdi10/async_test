from django.contrib import admin
from movie.models import *

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
   list_display = ('id', "title", "category", 'uid', "day")


admin.site.register(Movie, MovieAdmin)