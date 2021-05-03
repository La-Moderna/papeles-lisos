# Create your views here.
from rest_framework import mixins, viewsets, status
from utils.mixins import BaseGenericViewSet
from companies import serializers, models

from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from app.urls import router


class CompanyViewSet(mixins.CreateModelMixin,
                     viewsets.ViewSet,
                     BaseGenericViewSet):
    serializer_class = serializers.CompanySerializer
    queryset = models.Company.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        company_serializer = serializers.CompanySerializer(queryset, many=True)

        if company_serializer.is_valid():
            return Response(company_serializer.data)
        return Response(company_serializer.errors)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        user = get_object_or_404(queryset, id=pk)
        serializer = serializers.CompanySerializer(user)

        return Response(serializer.data)


router.register(
    r'companies',
    CompanyViewSet,
    basename='company'
)
