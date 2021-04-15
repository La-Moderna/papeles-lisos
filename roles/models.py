from django.db import models

# Create your models here.


class Role(models.Model):
    """Custom rol model to be used accross the app"""
    class Meta:
        """Define the behavior of the model"""
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        ordering = ('id',)

    ADM = 1
    AGE = 2
    CST = 3
    CXC = 4
    DIR = 5
    EMB = 6
    FAC = 7
    FEC = 8
    ING = 9

    ROLE_CHOICES = (
        (ADM, 'Administrador'),
        (AGE, 'Agente'),
        (CST, 'Costos'),
        (CXC, 'Direccion'),
        (EMB, 'Embarques'),
        (FAC, 'Facturacion'),
        (FEC, 'Fechas'),
        (ING, 'Ingenieria'),
    )
    id = models.AutoField(
        primary_key=True,
        verbose_name='ID'
    )
    is_active = models.BooleanField(
         default=False
     )

    name = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.get_name_display()
