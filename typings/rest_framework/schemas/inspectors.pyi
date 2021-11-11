"""
This type stub file was generated by pyright.
"""

"""
inspectors.py   # Per-endpoint view introspection

See schemas.__init__.py for package overview.
"""
class ViewInspector:
    """
    Descriptor class on APIView.

    Provide subclass for per-view schema generation
    """
    header_regex = ...
    def __init__(self) -> None:
        ...
    
    def __get__(self, instance, owner): # -> Self@ViewInspector:
        """
        Enables `ViewInspector` as a Python _Descriptor_.

        This is how `view.schema` knows about `view`.

        `__get__` is called when the descriptor is accessed on the owner.
        (That will be when view.schema is called in our case.)

        `owner` is always the owner class. (An APIView, or subclass for us.)
        `instance` is the view instance or `None` if accessed from the class,
        rather than an instance.

        See: https://docs.python.org/3/howto/descriptor.html for info on
        descriptor usage.
        """
        ...
    
    def __set__(self, instance, other): # -> None:
        ...
    
    @property
    def view(self):
        """View property."""
        ...
    
    @view.setter
    def view(self, value): # -> None:
        ...
    
    @view.deleter
    def view(self): # -> None:
        ...
    
    def get_description(self, path, method): # -> str:
        """
        Determine a path description.

        This will be based on the method docstring if one exists,
        or else the class docstring.
        """
        ...
    


class DefaultSchema(ViewInspector):
    """Allows overriding AutoSchema using DEFAULT_SCHEMA_CLASS setting"""
    def __get__(self, instance, owner): # -> ViewInspector:
        ...
    

