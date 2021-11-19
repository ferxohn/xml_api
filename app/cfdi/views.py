from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import CFDIIssued, CFDIReceived
from cfdi import serializers


class BaseCFDIAttrViewSet(viewsets.GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin):
    """Base viewset for issued CFDI attributes"""
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class CFDIIssuedViewSet(BaseCFDIAttrViewSet):
    "Manage issued CFDIs in the database"
    queryset = CFDIIssued.objects.all()
    serializer_class = serializers.CFDIIssuedSerializer

    def get_queryset(self):
        """"Return objects for the current client only"""
        # assigned_only = bool(
        #     int(self.request.query_params.get('assigned_only', 0))
        # )
        # queryset = self.queryset
        # if assigned_only:
        #     queryset = queryset.filter(recipe__isnull=False)

        return self.queryset.filter(
            user=self.request.user
        ).order_by('-name')

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(user=self.request.user)