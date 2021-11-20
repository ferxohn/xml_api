from rest_framework import serializers

from core.models import Client


class ClientSerializer(serializers.ModelSerializer):
    """Serializer for client object"""

    class Meta:
        model = Client
        fields = ('id', 'rfc', 'razon_social', )
        read_only_fields = ('id', )