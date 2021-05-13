
# """User API."""
# from django.shortcuts import get_object_or_404


from inventories import serializers
from inventories.models import Inventory
from inventories.models import Warehouse


from rest_framework import mixins, viewsets
from rest_framework.response import Response

from utils.mixins import BaseGenericViewSet

from app.urls import router


class WarehouseViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet,
                       BaseGenericViewSet):
    """Manage Creation of a Warehouse"""

    serializer_class = serializers.WarehouseSerializer
    retrieve_serializer_class = serializers.RetrieveWarehouseSerializer
    delete_serializer_class = serializers.DeleteWarehouseSerializer
    # permission_classes = [IsAuthenticated]

    queryset = Warehouse.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, action='retrieve')
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """Override destroy method, update status is_active to false"""
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        serializer = self.get_serializer(
            instance,
            action='delete')
        return Response(serializer.data)

    def perform_update_w(self, serializer):
        serializer.save()


class InventoryViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet,
                       BaseGenericViewSet):

    serializer_class = serializers.InventorySerializer
    retrieve_serializer_class = serializers.RetrieveInventorySerializer
    delete_serializer_class = serializers.DeleteInventorySerializer

    queryset = Inventory.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, action='retrieve')
        return Response(serializer.data)

    # forma provisional de hacerlo, no se si es la mejor opcion
    def destroy(self, request, *args, **kwargs):
        """Override destroy method, update status is_active to false"""
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        print(instance)
        serializer = self.get_serializer(
            instance,
            action='delete')
        return Response(serializer.data)

    def perform_update_i(self, serializer):
        serializer.save()


router.register(
    r'inventories',
    InventoryViewSet,
    basename="inventories",
)
router.register(
    r'warehouses',
    WarehouseViewSet,
    basename="warehouses",
)
