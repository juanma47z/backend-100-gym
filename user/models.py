from django.db import models

class Coach(models.Model):
    name = models.CharField(max_length=100, verbose_name='nombre')
    last_name = models.CharField(max_length=100, verbose_name='apellido')
    email = models.EmailField(verbose_name='email')
    cell_phone = models.CharField(max_length=10, verbose_name='telefono')

    class Meta:
        verbose_name = 'entrenador'
        verbose_name_plural = "entrenadores"

    def __str__(self):
        return self.name
        
class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name='nombre')
    last_name = models.CharField(max_length=100, verbose_name='apellido')
    email = models.EmailField(verbose_name='email')
    cell_phone = models.CharField(max_length=10, verbose_name='telefono')

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    
