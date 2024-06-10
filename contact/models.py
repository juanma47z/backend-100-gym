from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='nombre')
    email = models.EmailField()
    content = models.TextField()

    class Meta:
        verbose_name = 'formulario de contacto'
        verbose_name_plural = 'formularios de contacto'

    def __str__(self):
        return self.name
