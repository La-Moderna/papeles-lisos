from django.db import models  # noqa


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100, null=False)
    isActive = models.BooleanField(default=True, null=False)

    @staticmethod
    def loadCSV(self, csv):
        

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.name}, Activo: {self.isActive}"

    class Meta:
        ordering = ['id']
