from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

USER = get_user_model()


class CustomBackend(ModelBackend):
    """
    Define a new authentication backend for auth with username/password or email/password.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(USER.USERNAME_FIELD)

        users = USER._default_manager.filter(Q(username__exact=username) | Q(email__exact=username) |
                                             Q(phone_number__exact=username))

        # Test whether any matched user has the provided password:
        for user in users:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        if not users:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (see
            # https://code.djangoproject.com/ticket/20760)
            USER().set_password(password)
