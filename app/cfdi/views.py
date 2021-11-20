from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import CFDIIssued, CFDIReceived
from cfdi import serializers


class BaseCFDIAttrViewSet(viewsets.ModelViewSet):
    """Base viewset for CFDI attributes"""
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class CFDIIssuedViewSet(BaseCFDIAttrViewSet):
    "Manage issued CFDIs in the database"
    queryset = CFDIIssued.objects.all()
    serializer_class = serializers.CFDIIssuedSerializer


class CFDIReceivedViewSet(BaseCFDIAttrViewSet):
    "Manage received CFDIs in the database"
    queryset = CFDIReceived.objects.all()
    serializer_class = serializers.CFDIReceivedSerializer
