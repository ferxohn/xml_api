from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Client
from client import serializers


class ClientViewSet(viewsets.ModelViewSet):
    """Base viewset for client attributes"""
    queryset = Client.objects.all()
    serializer_class = serializers.ClientSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
        