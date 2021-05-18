from django.db import models

from utils.models import ActiveMixin


class Company(ActiveMixin):
    id = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=70)
