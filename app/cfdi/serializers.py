from rest_framework import serializers

from core.models import CFDIIssued, CFDIReceived


class CFDIIssuedSerializer(serializers.ModelSerializer):
    """Serializer for issued CFDI object"""

    class Meta:
        model = CFDIIssued
        fields = ('id', 'RFC_emisor', 'RFC_receptor', 'fecha', 'uuid', )
        read_only_fields = ('id', )