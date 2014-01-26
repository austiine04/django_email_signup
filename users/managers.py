from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password):
        return self._create_user(email, password)

    def create_superuser(self, email, password):
        return self._create_user(email, password, True, True)

    def _create_user(self, email, password, is_staff=False, is_superuser=False):
        self._check_for_email_and_password(email, password)
        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, is_superuser=is_superuser)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def _check_for_email_and_password(self, email, password):
        if not email:
            self._raise_value_error_exception("Cannot create user without email")
        if not password:
            self._raise_value_error_exception("Cannot create user without password")

    def _raise_value_error_exception(self, message):
        raise ValueError(message)


