from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from oscar.apps.customer.utils import normalise_email

User = get_user_model()


class EmailBackend(ModelBackend):
    """Custom auth backend that uses an email address and password.
    """
    def authenticate(self, email=None, password=None, *args, **kwargs):
        # Some auth backends expect to authenticate by ``username``.
        if email is None:
            if 'username' not in kwargs or kwargs['username'] is None:
                return None
            clean_email = normalise_email(kwargs['username'])
        else:
            clean_email = normalise_email(email)

        # Confirm that we're dealing with an email address.
        if '@' not in clean_email:
            return None

        # We make a case-insensitive match when looking for emails.
        matching_users = User.objects.filter(email__iexact=clean_email)
        authenticated_users = [
            user for user in matching_users if user.check_password(password)]
        if len(authenticated_users) == 1:
            # Happy path
            return authenticated_users[0]
        elif len(authenticated_users) > 1:
            # This is the problem scenario where we have multiple users with
            # the same email address AND password. We can't safely authenticate
            # either.
            raise User.MultipleObjectsReturned(
                "There are multiple users with the given email address and "
                "password")
        return None