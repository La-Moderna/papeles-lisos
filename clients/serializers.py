from clients.models import Agent
from clients.models import ClientsBalance

from rest_framework import serializers


class AgentSerializer(serializers.ModelSerializer):
    """Serializer for Agent Model."""

    class Meta:
        model = Agent
        fields = ('__all__',)


class ClientsBalanceSerializer(serializers.ModelSerializer):
    """Serializer for ClientsBalance Model."""

    class Meta:
        model = ClientsBalance
        fields = ('__all__',)
