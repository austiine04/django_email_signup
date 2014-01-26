from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy
from users.managers import CustomUserManager
from django.db import models

class User(AbstractBaseUser, PermissionsMixin):

    class Meta:
        app_label = 'users'
        verbose_name = 'user'
        verbose_name_plural = 'users'

    email = models.EmailField(max_length=45, unique=True)
    joining_date = models.DateTimeField(default=timezone.now())
    is_staff = models.BooleanField(ugettext_lazy("staff status"), default=False,
                                   help_text=('Designates whether can log into admin site'))

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.email

    def get_absolute_url(self):
        return "/users/%d" % self.id




