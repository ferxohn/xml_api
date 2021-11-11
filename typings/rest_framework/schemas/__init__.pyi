"""
This type stub file was generated by pyright.
"""

from rest_framework.settings import api_settings
from . import coreapi, openapi
from .coreapi import AutoSchema, ManualSchema, SchemaGenerator
from .inspectors import DefaultSchema

"""
rest_framework.schemas

schemas:
    __init__.py
    generators.py   # Top-down schema generation
    inspectors.py   # Per-endpoint view introspection
    utils.py        # Shared helper functions
    views.py        # Houses `SchemaView`, `APIView` subclass.

We expose a minimal "public" API directly from `schemas`. This covers the
basic use-cases:

    from rest_framework.schemas import (
        AutoSchema,
        ManualSchema,
        get_schema_view,
        SchemaGenerator,
    )

Other access should target the submodules directly
"""
def get_schema_view(title=..., url=..., description=..., urlconf=..., renderer_classes=..., public=..., patterns=..., generator_class=..., authentication_classes=..., permission_classes=..., version=...): # -> (*args: Any, **kwargs: Any) -> HttpResponseBase:
    """
    Return a schema view.
    """
    ...

