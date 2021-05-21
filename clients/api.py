# Create your views here.
from clients import models, serializers

from rest_framework import viewsets

from utils.mixins import (
    BaseGenericViewSet,
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin
)

from app.urls import router


class AgentViewSet(ListModelMixin,
                   CreateModelMixin,
                   RetrieveModelMixin,
                   UpdateModelMixin,
                   DestroyModelMixin,
                   viewsets.GenericViewSet,
                   BaseGenericViewSet):
    """Manage Agents."""

    serializer_class = serializers.AgentSerializer
    list_serializer_class = serializers.AgentSerializer
    create_serializer_class = serializers.CreateAgentSerializer
    retrieve_serializer_class = serializers.CreateAgentSerializer
    update_serializer_class = serializers.UpdateAgentSerializer

    queryset = models.Agent.objects.filter(is_active=True)


class BalanceViewSet(ListModelMixin,
                     CreateModelMixin,
                     RetrieveModelMixin,
                     UpdateModelMixin,
                     DestroyModelMixin,
                     viewsets.GenericViewSet,
                     BaseGenericViewSet):
    """Manage Balance."""

    serializer_class = serializers.BalanceSerializer
    list_serializer_class = serializers.BalanceSerializer
    create_serializer_class = serializers.CreateBalanceSerializer
    retrieve_serializer_class = serializers.CreateBalanceSerializer
    update_serializer_class = serializers.UpdateBalanceSerializer

    queryset = models.Balance.objects.filter(is_active=True)


router.register(
    r'clients/agents',
    AgentViewSet,
    basename="agent"
)

router.register(
    r'clients/balance',
    BalanceViewSet,
    basename="balance"
)
