from django.test import TestCase
from users.forms import SignupForm


class SignupFormTest(TestCase):

    def test_cannot_submit_empty_signup_form(self):
        signup_form = SignupForm(data = {})
        self.assertFalse(signup_form.is_valid())

    def test_form_should_not_have_a_username_field(self):
        signup_form = SignupForm(data = {})
        with self.assertRaises(KeyError):
            signup_form.fields['username']

    def test_form_should_have_email_address_field(self):
        signup_form = SignupForm(data = {})
        self.failUnless(signup_form.fields['email'])

    def test_form_should_not_allow_empty_passowrds(self):
        signup_form = SignupForm(data = {'email':'email@shop.com'})
        self.assertFalse(signup_form.is_valid())

    def test_form_should_be_valid_given_matching_passwords(self):
        data = {'email': 'email@shop.com', 'password1': 'password1234', 'password2': 'password1234'}
        signup_form = SignupForm(data=data)
        self.assertTrue(signup_form.is_valid())

    def test_form_should_not_be_valid_given_different_passwords(self):
        data = {'email': 'email@shop.com', 'password1': 'password1234', 'password2': 'password12345'}
        signup_form = SignupForm(data=data)
        self.assertFalse(signup_form.is_valid())

    def test_form_should_be_invalid_given_email_address_without_domain_part(self):
        data = {'email': 'email', 'password1': 'password1234', 'password2': 'password1234'}
        signup_form = SignupForm(data=data)
        self.assertFalse(signup_form.is_valid())

    def test_form_should_be_invalid_given_email_without_extension(self):
        data = {'email': 'email@shop', 'password1': 'password1234', 'password2': 'password1234'}
        signup_form = SignupForm(data=data)
        self.assertFalse(signup_form.is_valid())

    def test_form_should_be_invalid_given_email_address_and_password1_only(self):
        data = {'email': 'email@shop', 'password1': 'password1234'}
        signup_form = SignupForm(data=data)
        self.assertFalse(signup_form.is_valid())

    def test_form_should_be_invalid_given_email_address_and_password2_only(self):
        data = {'email': 'email@shop.com', 'password2': 'password1234'}
        signup_form = SignupForm(data=data)
        self.assertFalse(signup_form.is_valid())