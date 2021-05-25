from django.shortcuts import get_object_or_404

from inventories import models, serializers

from rest_framework import viewsets

from utils.mixins import (
    BaseGenericViewSet,
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)

from app.urls import router


class ItemViewSet(ListModelMixin,
                  CreateModelMixin,
                  RetrieveModelMixin,
                  UpdateModelMixin,
                  DestroyModelMixin,
                  viewsets.GenericViewSet,
                  BaseGenericViewSet):

    serializer_class = serializers.ItemSerializer
    create_serializer_class = serializers.CreateItemSerializer
    list_serializer_class = serializers.RetrieveItemSerializer
    retrieve_serializer_class = serializers.RetrieveItemSerializer
    update_serializer_class = serializers.CreateItemSerializer

    queryset = models.Item.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {'item_id': self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)

        self.check_object_permissions(self.request, obj)

        return obj


router.register(
    r'items',
    ItemViewSet,
    'item'
)
