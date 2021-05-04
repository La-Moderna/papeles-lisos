# Create your views here.
from clients import serializers

from rest_framework import mixins, viewsets

from utils.mixins import BaseGenericViewSet

from app.urls import router


class AgentViewSet(mixins.CreateModelMixin,
                   viewsets.GenericViewSet,
                   BaseGenericViewSet):
    """Manage Agents."""
    serializer_class = serializers.AgentSerializer


class ClientBalanceViewSet(mixins.CreateModelMixin,
                           viewsets.GenericViewSet,
                           BaseGenericViewSet):
    """Manage ClientsBalance."""
    serializer_class = serializers.ClientsBalanceSerializer


router.register(
    r'clients/agents',
    AgentViewSet,
    basename="agent"
)

router.register(
    r'clients/clientsBalance',
    ClientBalanceViewSet,
    basename="clientsBalance"
)
