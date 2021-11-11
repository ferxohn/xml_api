"""
This type stub file was generated by pyright.
"""

"""
Settings for REST framework are all namespaced in the REST_FRAMEWORK setting.
For example your project's `settings.py` file might look like this:

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.TemplateHTMLRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
}

This module provides the `api_setting` object, that is used to access
REST framework settings, checking for user settings first, then falling
back to the defaults.
"""
DEFAULTS = ...
IMPORT_STRINGS = ...
REMOVED_SETTINGS = ...
def perform_import(val, setting_name): # -> Any | list[Any] | None:
    """
    If the given setting is a string import notation,
    then perform the necessary import or imports.
    """
    ...

def import_from_string(val, setting_name): # -> Any:
    """
    Attempt to import a class from a string representation.
    """
    ...

class APISettings:
    """
    A settings object that allows REST Framework settings to be accessed as
    properties. For example:

        from rest_framework.settings import api_settings
        print(api_settings.DEFAULT_RENDERER_CLASSES)

    Any setting with string import paths will be automatically resolved
    and return the class, rather than the string literal.

    Note:
    This is an internal class that is only compatible with settings namespaced
    under the REST_FRAMEWORK name. It is not intended to be used by 3rd-party
    apps, and test helpers like `override_settings` may not work as expected.
    """
    def __init__(self, user_settings=..., defaults=..., import_strings=...) -> None:
        ...
    
    @property
    def user_settings(self): # -> Any | Unknown | dict[Unknown, Unknown]:
        ...
    
    def __getattr__(self, attr): # -> Any | list[Any] | dict[str, None] | bool | int | dict[str, str] | list[str] | str | list[Unknown] | None:
        ...
    
    def reload(self): # -> None:
        ...
    


api_settings = ...
def reload_api_settings(*args, **kwargs): # -> None:
    ...

