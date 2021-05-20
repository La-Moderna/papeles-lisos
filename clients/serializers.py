from clients.models import Agent
from clients.models import Balance

from django.core.exceptions import ValidationError

from rest_framework import serializers


class AgentSerializer(serializers.ModelSerializer):
    """Serializer for Agent Model."""

    class Meta:
        model = Agent
        fields = ('__all__')


class CreateAgentSerializer(serializers.ModelSerializer):
    """Serializer for Agent Model."""

    class Meta:
        model = Agent
        fields = [
            'representant',
            'company'
        ]


class UpdateAgentSerializer(serializers.ModelSerializer):
    """Serializer for Agent Model."""
    def validate_representant(self, representant):
        if len(representant) < 1:
            raise ValidationError(
                'Representant must have at least one character'
            )

        return representant

    class Meta:
        model = Agent
        fields = [
            'representant'
        ]


class BalanceSerializer(serializers.ModelSerializer):
    """Serializer for Balance Model."""

    class Meta:
        model = Balance
        fields = ('__all__')


class CreateBalanceSerializer(serializers.ModelSerializer):
    """Serializer for Balance Model."""

    class Meta:
        model = Balance
        fields = [
            'order_balance',
            'facture_balance',
            'company'
        ]


class UpdateBalanceSerializer(serializers.ModelSerializer):
    """Serializer for Balance Model."""
    def validate_representant(self, representant):
        if len(representant) < 1:
            raise ValidationError(
                'Order Balance must have at least one number'
            )

        return representant

    class Meta:
        model = Balance
        fields = [
            'order_balance',
            'facture_balance'
        ]
