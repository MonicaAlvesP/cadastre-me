from django.db import models

class Usuario(models.Model):
  id_usuario = models.AutoField(primary_key=True) # Criando um campo auto incrementável
  nome = models.CharField(max_length=255) # Criando um campo de texto com 100 caracteres
  idade = models.IntegerField() # Criando um campo de número inteiro