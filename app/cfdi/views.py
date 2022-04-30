from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import CFDIIssued, CFDIReceived
from cfdi import serializers


class BaseCFDIAttrViewSet(viewsets.ModelViewSet):
    """Base viewset for CFDI attributes"""
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def _params_to_ints(self, qs):
        """Convert a list of strings to a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """Retrieve CFDIs for the selected client"""
        client = self.request.query_params.get('client')
        queryset = self.queryset
        if client:
            client_id = self._params_to_ints(client)
            queryset = queryset.filter(client__id__in=client_id)
        return queryset


class CFDIIssuedViewSet(BaseCFDIAttrViewSet):
    "Manage issued CFDIs in the database"
    queryset = CFDIIssued.objects.all()
    serializer_class = serializers.CFDIIssuedSerializer


class CFDIReceivedViewSet(BaseCFDIAttrViewSet):
    "Manage received CFDIs in the database"
    queryset = CFDIReceived.objects.all()
    serializer_class = serializers.CFDIReceivedSerializer
