from django.db import models

# Create your models here.
# AQUI QUE TRABALHAMOS COM BANCO DE DADOS CUZÃO.

class Usuario(models.Model): 
    # Aqui criamos a tabela dos usuarios, usando model para montala
        #temos nosso Id, Text e Int bonitinhos.
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=250)
    idade = models.IntegerField()
