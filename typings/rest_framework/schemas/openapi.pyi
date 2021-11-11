"""
This type stub file was generated by pyright.
"""

from .generators import BaseSchemaGenerator
from .inspectors import ViewInspector

class SchemaGenerator(BaseSchemaGenerator):
    def get_info(self): # -> dict[str, Unknown | str]:
        ...
    
    def check_duplicate_operation_id(self, paths): # -> None:
        ...
    
    def get_schema(self, request=..., public=...):
        """
        Generate a OpenAPI schema.
        """
        ...
    


class AutoSchema(ViewInspector):
    def __init__(self, tags=..., operation_id_base=..., component_name=...) -> None:
        """
        :param operation_id_base: user-defined name in operationId. If empty, it will be deducted from the Model/Serializer/View name.
        :param component_name: user-defined component's name. If empty, it will be deducted from the Serializer's class name.
        """
        ...
    
    request_media_types = ...
    response_media_types = ...
    method_mapping = ...
    def get_operation(self, path, method): # -> dict[Unknown, Unknown]:
        ...
    
    def get_component_name(self, serializer): # -> str:
        """
        Compute the component's name from the serializer.
        Raise an exception if the serializer's class name is "Serializer" (case-insensitive).
        """
        ...
    
    def get_components(self, path, method): # -> dict[Unknown | str, dict[str, str | dict[Unknown, Unknown]]]:
        """
        Return components with their properties from the serializer.
        """
        ...
    
    def get_operation_id_base(self, path, method, action):
        """
        Compute the base part for operation ID from the model, serializer or view name.
        """
        ...
    
    def get_operation_id(self, path, method): # -> Any | str:
        """
        Compute an operation ID from the view type and get_operation_id_base method.
        """
        ...
    
    def get_path_parameters(self, path, method):
        """
        Return a list of parameters from templated path variables.
        """
        ...
    
    def get_filter_parameters(self, path, method): # -> list[Unknown]:
        ...
    
    def allows_filters(self, path, method): # -> bool:
        """
        Determine whether to include filter Fields in schema.

        Default implementation looks for ModelViewSet or GenericAPIView
        actions/methods that cause filtering on the default implementation.
        """
        ...
    
    def get_pagination_parameters(self, path, method): # -> Any | list[Unknown]:
        ...
    
    def map_choicefield(self, field): # -> dict[str, list[Unknown]]:
        ...
    
    def map_field(self, field):
        ...
    
    def map_serializer(self, serializer):
        ...
    
    def map_field_validators(self, field, schema):
        """
        map field validators
        """
        ...
    
    def get_paginator(self): # -> Any | None:
        ...
    
    def map_parsers(self, path, method): # -> list[Any]:
        ...
    
    def map_renderers(self, path, method): # -> list[Unknown]:
        ...
    
    def get_serializer(self, path, method): # -> None:
        ...
    
    def get_request_body(self, path, method): # -> dict[str, dict[Any, dict[str, dict[str, str]]]]:
        ...
    
    def get_responses(self, path, method): # -> dict[str, dict[str, str]] | dict[str, dict[str, dict[Unknown, dict[str, Any | dict[str, str | dict[str, str]] | dict[str, str]]] | str]]:
        ...
    
    def get_tags(self, path, method): # -> list[Unknown]:
        ...
    


