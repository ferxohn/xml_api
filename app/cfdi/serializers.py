from rest_framework import serializers

from core.models import CFDIIssued, CFDIReceived


class CFDIIssuedSerializer(serializers.ModelSerializer):
    """Serializer for an issued CFDI object"""

    class Meta:
        model = CFDIIssued
        fields = (
            'id',
            'client',
            'rfc_receptor',
            'razon_social_receptor',
            'fecha',
            'uuid',
            'serie',
            'folio',
            'version',
            'lugar_expedicion',
            'metodo_pago',
            'tipo_comprobante',
            'moneda',
            'total',
            'subtotal',
            'forma_pago',
            'xml_path',
        )
        read_only_fields = ('id', )


class CFDIReceivedSerializer(serializers.ModelSerializer):
    """Serializer for a received CFDI object"""

    class Meta:
        model = CFDIReceived
        fields = (
            'id',
            'client',
            'rfc_emisor',
            'razon_social_emisor',
            'fecha',
            'uuid',
            'serie',
            'folio',
            'version',
            'lugar_expedicion',
            'metodo_pago',
            'tipo_comprobante',
            'moneda',
            'total',
            'subtotal',
            'forma_pago',
            'xml_path',
        )
        read_only_fields = ('id', )
