from django.db import models
from datetime import date 

# Create your models here.

class Usuario(models.Model): #cadastro usuario
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=64)
           
    def __str__(self) -> str:
        return self.nome
   
class Livro(models.Model):#cadastro livro
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    editora = models.CharField(max_length=50)
    data_cadastro = models.DateField(default = date.today) # data automática
           
    def __str__(self) -> str:
        return self.titulo