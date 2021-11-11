"""
This type stub file was generated by pyright.
"""

import functools
import json

"""
Wrapper for the builtin json module that ensures compliance with the JSON spec.

REST framework should always import this wrapper module in order to maintain
spec-compliant encoding/decoding. Support for non-standard features should be
handled by users at the renderer and parser layer.
"""
def strict_constant(o): # -> NoReturn:
    ...

@functools.wraps(json.dump)
def dump(*args, **kwargs): # -> None:
    ...

@functools.wraps(json.dumps)
def dumps(*args, **kwargs): # -> str:
    ...

@functools.wraps(json.load)
def load(*args, **kwargs): # -> Any:
    ...

@functools.wraps(json.loads)
def loads(*args, **kwargs): # -> Any:
    ...

