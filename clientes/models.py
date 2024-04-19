from django.db import models

class Clientes(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=100, blank=True)
    telefone = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Clientes"
    
    def __str__(self):
        return self.nome
