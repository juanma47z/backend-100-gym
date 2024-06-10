from django.db import models
from user.models import Coach

class Services(models.Model):
    title = models.CharField(max_length=200, verbose_name='titulo')
    content = models.TextField(verbose_name='contenido')
    price = models.DecimalField(max_digits=8,decimal_places=2 ,verbose_name='precio')
    coach = models.ManyToManyField(Coach, verbose_name='entrenador')
    created = models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateField(auto_now=True, verbose_name='Fecha de modificacion')

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ['-created']

    def __str__(self):
        return self.title