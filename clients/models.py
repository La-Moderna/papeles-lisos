from django.db import models

from utils.models import ActiveMixin


class Agent(ActiveMixin):
    representant = models.CharField(max_length=45)
    # company = models.ForeignKey()

    def __str__(self):
        return self.headline


class ClientsBalance(ActiveMixin):
    # company = models.ForeignKey
    client = models.CharField(max_length=40)
    orderBalance = models.CharField(max_length=45)
    factureBalance = models.CharField(max_length=45)
