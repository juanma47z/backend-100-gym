from django.db import models

class Link(models.Model):
    key = models.SlugField(verbose_name='clave', unique=True)
    name = models.CharField(verbose_name='nombre', max_length=200)
    url = models.URLField(verbose_name='enlace', max_length=200, null=True, blank=True)
    created = models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')
    updated = models.DateField(auto_now=True, verbose_name='Fecha de modificacion')

    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"

    def __str__(self):
        return self.name