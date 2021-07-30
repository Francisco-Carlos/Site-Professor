from django.contrib import admin

# Register your models here.
from .models import Conteudos

class Lista_Conteudos(admin.ModelAdmin):
    list_display = ('id','Nome')

admin.site.register(Conteudos,Lista_Conteudos)