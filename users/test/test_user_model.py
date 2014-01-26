import datetime
from unittest import TestCase
from django.utils import timezone
from mockito import mock, when
from users.models import User


class UserTest(TestCase):

    def setUp(self):
        self.email = "shop@email.com"
        self.user = User(id=23, email=self.email, password="password")

    def test_user_has_user_name(self):
       self.assertEquals(self.user.get_username(), self.email)

    def test_user_has_password(self):
        self.assertTrue(self.user.password == "password")

    def test_user_has_full_name(self):
        self.assertEquals(self.user.get_full_name(), self.email)

    def test_user_has_unicode_string(self):
        self.assertEquals(self.user.__unicode__(), "%s" % self.email)

    def test_user_has_absolute_url(self):
        self.assertEquals(self.user.get_absolute_url(), "/users/23")

    def test_user_has_joining_date(self):
        #TODO: implement this test
        pass



