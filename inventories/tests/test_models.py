""" Tests for users of the application."""


from django.db import transaction
from django.db.utils import DataError, IntegrityError
from django.test import TestCase

from inventories.models import Inventory
from inventories.models import Warehouse


class InventoryTestCase(TestCase):
    "Test Inventory model."
    def setUp(self):
        self.warehouse = Warehouse.objects.create(
            description="Test warehouse exception"
        )
        self.inventory = Inventory.objects.create(
            stock='2000', warehouse=self.warehouse
        )

    def test_max_length(self):
        """Test max_length values."""
        inventory = self.inventory
        with transaction.atomic():
            inventory.stock = 4.0*2550000000000
            with self.assertRaises(DataError):
                inventory.save()

        with transaction.atomic():
            inventory.warehouse.description = 'x'*101
            with self.assertRaises(DataError):
                inventory.save()

    def test_not_nulls(self):
        """Test not_null fields."""
        warehouse = self.warehouse
        inventory = self.inventory

        with transaction.atomic():
            warehouse.description = None
            with self.assertRaises(IntegrityError):
                warehouse.save()

        with transaction.atomic():
            inventory.warehouse = None
            with self.assertRaises(IntegrityError):
                inventory.save()
