# Django
from django.test import TestCase

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status

# Models
from users.models import User

class CompanyTestEndpoints(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            name="PELICULAS PLASTICAS SA DE CV"
        )

    def test_get_companies(self):
        