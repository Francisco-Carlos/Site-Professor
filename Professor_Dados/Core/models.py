from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Conteudos(models.Model):
    Nome = models.CharField(max_length=200)
    Conteudo = models.TextField()
    Arquivo = models.FileField(upload_to='arquivos/%d/%m/%Y', blank=True)
    Criador = models.ForeignKey(User,on_delete=models.CASCADE)