from django.db import models

# Create your models here.


class Almacen(models.Model):

    class Meta:
        """Define the behavior of the model."""

        verbose_name = 'Almacen'
        verbose_name_plural = 'Almacenes'

    company = models.CharField(
        max_length=4,
        unique=True,
        verbose_name='compañia'
    )
    almacen = models.CharField(
        max_length=4,
        verbose_name='almacen'
    )

    def __str__(self):
        """Return the representation in string"""
        return self.almacen
