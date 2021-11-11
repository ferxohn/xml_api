"""
This type stub file was generated by pyright.
"""

"""
Parsers are used to parse the content of incoming HTTP requests.

They give us a generic way of being able to handle various media types
on the request, such as form content or json encoded data.
"""
class DataAndFiles:
    def __init__(self, data, files) -> None:
        ...
    


class BaseParser:
    """
    All parsers should extend `BaseParser`, specifying a `media_type`
    attribute, and overriding the `.parse()` method.
    """
    media_type = ...
    def parse(self, stream, media_type=..., parser_context=...):
        """
        Given a stream to read from, return the parsed representation.
        Should return parsed data, or a `DataAndFiles` object consisting of the
        parsed data and files.
        """
        ...
    


class JSONParser(BaseParser):
    """
    Parses JSON-serialized data.
    """
    media_type = ...
    renderer_class = ...
    strict = ...
    def parse(self, stream, media_type=..., parser_context=...): # -> Any:
        """
        Parses the incoming bytestream as JSON and returns the resulting data.
        """
        ...
    


class FormParser(BaseParser):
    """
    Parser for form data.
    """
    media_type = ...
    def parse(self, stream, media_type=..., parser_context=...): # -> QueryDict:
        """
        Parses the incoming bytestream as a URL encoded form,
        and returns the resulting QueryDict.
        """
        ...
    


class MultiPartParser(BaseParser):
    """
    Parser for multipart form data, which may include file data.
    """
    media_type = ...
    def parse(self, stream, media_type=..., parser_context=...): # -> DataAndFiles:
        """
        Parses the incoming bytestream as a multipart encoded form,
        and returns a DataAndFiles object.

        `.data` will be a `QueryDict` containing all the form parameters.
        `.files` will be a `QueryDict` containing all the form files.
        """
        ...
    


class FileUploadParser(BaseParser):
    """
    Parser for file upload data.
    """
    media_type = ...
    errors = ...
    def parse(self, stream, media_type=..., parser_context=...):
        """
        Treats the incoming bytestream as a raw file upload and returns
        a `DataAndFiles` object.

        `.data` will be None (we expect request body to be a file content).
        `.files` will be a `QueryDict` containing one 'file' element.
        """
        ...
    
    def get_filename(self, stream, media_type, parser_context):
        """
        Detects the uploaded file name. First searches a 'filename' url kwarg.
        Then tries to parse Content-Disposition header.
        """
        ...
    
    def get_encoded_filename(self, filename_parm): # -> str:
        """
        Handle encoded filenames per RFC6266. See also:
        https://tools.ietf.org/html/rfc2231#section-4
        """
        ...
    


