"""
This type stub file was generated by pyright.
"""

"""
Helpers for dealing with HTML input.
"""
def is_html_input(dictionary): # -> bool:
    ...

def parse_html_list(dictionary, prefix=..., default=...): # -> list[Unknown]:
    """
    Used to support list values in HTML forms.
    Supports lists of primitives and/or dictionaries.

    * List of primitives.

    {
        '[0]': 'abc',
        '[1]': 'def',
        '[2]': 'hij'
    }
        -->
    [
        'abc',
        'def',
        'hij'
    ]

    * List of dictionaries.

    {
        '[0]foo': 'abc',
        '[0]bar': 'def',
        '[1]foo': 'hij',
        '[1]bar': 'klm',
    }
        -->
    [
        {'foo': 'abc', 'bar': 'def'},
        {'foo': 'hij', 'bar': 'klm'}
    ]

    :returns a list of objects, or the value specified in ``default`` if the list is empty
    """
    ...

def parse_html_dict(dictionary, prefix=...): # -> MultiValueDict[Unknown, Unknown]:
    """
    Used to support dictionary values in HTML forms.

    {
        'profile.username': 'example',
        'profile.email': 'example@example.com',
    }
        -->
    {
        'profile': {
            'username': 'example',
            'email': 'example@example.com'
        }
    }
    """
    ...

