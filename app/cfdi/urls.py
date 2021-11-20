from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cfdi import views

router = DefaultRouter()
router.register('issued', views.CFDIIssuedViewSet)
router.register('received', views.CFDIReceivedViewSet)

app_name = 'cfdi'

urlpatterns = [
    path('', include(router.urls))
]
