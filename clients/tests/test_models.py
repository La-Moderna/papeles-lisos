""" Tests for clients of the application."""

# from unittest import mock

from clients.models import Agent, ClientsBalance

from django.db import transaction
from django.db.utils import DataError, IntegrityError
from django.test import TestCase


class AgentTestCase(TestCase):
    "Test Agent model."
    def setUp(self):
        self.user = Agent.objects.create(
            representant="Test agent exception"
        )

    def test_max_length(self):
        """Test max_length values."""
        user = self.user
        with transaction.atomic():
            user.representant = 'x'*46
            with self.assertRaises(DataError):
                user.save()

    def test_not_nulls(self):
        """Test not_null fields."""
        user = self.user

        with transaction.atomic():
            user.representant = None
            with self.assertRaises(IntegrityError):
                user.save()


class ClientsBalanceTestCase(TestCase):
    "Test ClientsBalance model."
    def setUp(self):
        self.user = ClientsBalance.objects.create(
            client="Test clientsBalance exception"
        )

    def test_max_length(self):
        """Test max_length values."""
        user = self.user
        with transaction.atomic():
            user.client = 'x'*41
            with self.assertRaises(DataError):
                user.save()

        with transaction.atomic():
            user.factureBalance = 'x'*46
            with self.assertRaises(DataError):
                user.save()

        with transaction.atomic():
            user.factureBalance = 'x'*46
            with self.assertRaises(DataError):
                user.save()

    def test_not_nulls(self):
        """Test not_null fields."""
        user = self.user

        with transaction.atomic():
            user.client = None
            with self.assertRaises(IntegrityError):
                user.save()

        with transaction.atomic():
            user.orderBalance = None
            with self.assertRaises(IntegrityError):
                user.save()

        with transaction.atomic():
            user.factureBalance = None
            with self.assertRaises(IntegrityError):
                user.save()
