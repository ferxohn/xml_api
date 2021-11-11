"""
This type stub file was generated by pyright.
"""

from django.middleware.csrf import CsrfViewMiddleware

"""
Provides various authentication policies.
"""
def get_authorization_header(request): # -> bytes:
    """
    Return request's 'Authorization:' header, as a bytestring.

    Hide some test client ickyness where the header can be unicode.
    """
    ...

class CSRFCheck(CsrfViewMiddleware):
    ...


class BaseAuthentication:
    """
    All authentication classes should extend BaseAuthentication.
    """
    def authenticate(self, request):
        """
        Authenticate the request and return a two-tuple of (user, token).
        """
        ...
    
    def authenticate_header(self, request): # -> None:
        """
        Return a string to be used as the value of the `WWW-Authenticate`
        header in a `401 Unauthenticated` response, or `None` if the
        authentication scheme should return `403 Permission Denied` responses.
        """
        ...
    


class BasicAuthentication(BaseAuthentication):
    """
    HTTP Basic authentication against username/password.
    """
    www_authenticate_realm = ...
    def authenticate(self, request):
        """
        Returns a `User` if a correct username and password have been supplied
        using HTTP Basic authentication.  Otherwise returns `None`.
        """
        ...
    
    def authenticate_credentials(self, userid, password, request=...): # -> tuple[AbstractBaseUser, None]:
        """
        Authenticate the userid and password against username and password
        with optional request for context.
        """
        ...
    
    def authenticate_header(self, request): # -> str:
        ...
    


class SessionAuthentication(BaseAuthentication):
    """
    Use Django's session framework for authentication.
    """
    def authenticate(self, request): # -> tuple[Any, None] | None:
        """
        Returns a `User` if the request session currently has a logged in user.
        Otherwise returns `None`.
        """
        ...
    
    def enforce_csrf(self, request): # -> None:
        """
        Enforce CSRF validation for session based authentication.
        """
        ...
    


class TokenAuthentication(BaseAuthentication):
    """
    Simple token based authentication.

    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string "Token ".  For example:

        Authorization: Token 401f7ac837da42b97f613d789819ff93537bee6a
    """
    keyword = ...
    model = ...
    def get_model(self): # -> Type[Token]:
        ...
    
    def authenticate(self, request): # -> tuple[Any, Any] | None:
        ...
    
    def authenticate_credentials(self, key): # -> tuple[Any, Any]:
        ...
    
    def authenticate_header(self, request): # -> str:
        ...
    


class RemoteUserAuthentication(BaseAuthentication):
    """
    REMOTE_USER authentication.

    To use this, set up your web server to perform authentication, which will
    set the REMOTE_USER environment variable. You will need to have
    'django.contrib.auth.backends.RemoteUserBackend in your
    AUTHENTICATION_BACKENDS setting
    """
    header = ...
    def authenticate(self, request): # -> tuple[AbstractBaseUser, None] | None:
        ...
    


