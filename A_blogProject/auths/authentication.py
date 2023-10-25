from rest_framework.authentication import (
    SessionAuthentication as SessionAuthentication_,
    BaseAuthentication,
    CSRFCheck,
    get_authorization_header,
)
from rest_framework import HTTP_HEADER_ENCODING, exceptions
from django.utils.translation import gettext_lazy as _


# def authenticate(*args, **kwargs):
#   pass

from django.contrib.sessions.models import Session
from django.utils import timezone
from rest_framework import exceptions
from consumer.models import Consumer as User

# class LoginAuthentication(BaseAuthentication):

# def authenticate(self, request):

# sessionid = request._request.COOKIES.get("sessionid", None)
# # print(sessionid)
# if not sessionid:
#     return None


class SessionAuthentication(SessionAuthentication_):
    def authenticate(self, request):
        user = getattr(request._request, "user", None)
        if not user or not user.is_active:
            return None
        self.enforce_csrf(request)
        return (user, None)

    def enforce_csrf(self, request):
        def dummy_get_response(request):  # pragma: no cover
            return None

        check = CSRFCheck(dummy_get_response)
        check.process_request(request)
        reason = check.process_view(request, None, (), {})
        if reason:
            raise exceptions.PermissionDenied("CSRF Failed: %s" % reason)


class TokenAuthentication(BaseAuthentication):
    keyword = "Token"
    model = None

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None
        if len(auth) == 1:
            msg = _("Invalid token header. No credentials provided.")
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _("Invalid token header. Token string should not contain spaces.")
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _(
                "Invalid token header. Token string should not contain invalid characters."
            )
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related("user").get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_("Invalid token."))

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(_("User inactive or deleted."))

        return (token.user, token)

    def authenticate_header(self, request):
        return self.keyword
