from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    # phone = models.PhoneNumberField()
       
    def __str__(self) -> str:
        return self.nome
   
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
       
    def __str__(self) -> str:
        return self.titulo