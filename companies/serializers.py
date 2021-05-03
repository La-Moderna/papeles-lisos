from rest_framework import serializers
from companies.models import Company


class CompanySerializer(serializers.Serializer):
    """Serializer for Company"""

    class Meta:
        """Define the class behavior"""

        model = Company
        fields = '__all__'
