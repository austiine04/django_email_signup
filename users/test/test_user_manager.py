from django.db import IntegrityError
from django.test import TestCase
from django.utils import timezone
from mockito import mock, when
from model_mommy import mommy
from users.models import User

class UserManagerTest(TestCase):

    def test_can_create_user(self):
        User.objects.create_user("shop@email.com", "123")
        self.assertEquals(1, User.objects.count())
        user = User.objects.all()[0]
        self.assertEquals("shop@email.com", user.email)

    def test_can_not_create_user_with_out_password(self):
        with self.assertRaises(ValueError):
            User.objects.create_user("shop@email.com", "")

    def test_can_not_create_user_with_out_email(self):
        with self.assertRaises(ValueError):
            User.objects.create_user("", "")

    def test_user_manager_should_normalize_email_address(self):
        user = User.objects.create_user("shop@eMAil.cOm", "123")
        self.assertTrue(user.email == "shop@email.com")

    def test_create_user_should_hash_user_password(self):
        user = mommy.prepare(User)
        self.assertNotEquals(user.password, "123")

    def test_create_superuser_should_create_a_super_user(self):
        user = User.objects.create_superuser("admin@email.com", 123)
        self.assertTrue(user.is_superuser)

    def test_uniqueness_of_email_field(self):
        user = User(email="email@shop.com", password="123454367")
        user.save()
        with self.assertRaises(IntegrityError):
            User.objects.create_user("email@shop.com", "54367")

    def test_user_account_should_active_by_default(self):
        user = mommy.prepare(User)
        self.assertTrue(user.is_active)

    def test_user_should_have_joining_date(self):
        current_date = timezone.now()
        mock_timezone = mock(timezone)
        when(mock_timezone).now().thenReturn(current_date)
        user = mommy.prepare(User, joining_date=mock_timezone.now())
        self.assertEquals(current_date, user.joining_date)


