from django.contrib import admin
from .models import Reviews 

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    fields = ['title']

admin.site.register(Reviews, ArticleAdmin)