from companies import models, serializers

from django.shortcuts import get_object_or_404

from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from utils.mixins import BaseGenericViewSet

from app.urls import router


class CompanyViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet,
                     BaseGenericViewSet):

    serializer_class = serializers.CompanySerializer
    retrieve_serializer_class = serializers.RetriveCompanySerializer
    create_serializer_class = serializers.CreateCompanySerializer
    update_serializer_class = serializers.UpdateCompanySerializer
    queryset = models.Company.objects.all()

    def partial_update(self, request, pk=None):
        queryset = self.get_queryset()
        company_object = get_object_or_404(queryset, pk=pk)

        company_serializer = self.get_serializer(
            company_object,
            data=request.data,
            action='update',
            partial=True
        )

        if company_serializer.is_valid():
            if 'name' in request.data:
                company_object.name = request.data['name']

            if 'is_active' in request.data:
                company_object.is_active = request.data['is_active']

            company_object.save()
            return Response(
                company_serializer.data,
                status=status.HTTP_200_OK
            )

        else:
            return Response(
                company_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def destroy(self, request, *args, **kwargs):
        company = self.get_object()
        company.is_active = False
        company.save()

        serializer = self.get_serializer(company)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


router.register(
    r'companies',
    CompanyViewSet,
    'company'
)
