from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from users.forms import SignupForm
from users.models import User


class SignUpViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get_request_should_return_200(self):
        self.response = self.client.get(reverse('new_user_form'))
        self.assertEquals(200, self.response.status_code)

    def test_response_on_get_request_should_a_form_object(self):
        self.response = self.client.get(reverse('new_user_form'))
        self.assertIn('form', self.response.context)

    def test_form_object_in_response_context_should_be_of_type_signupform(self):
        self.response = self.client.get(reverse('new_user_form'))
        self.assertTrue(isinstance(self.response.context['form'], SignupForm))

    def test_get_request_renders_signup_form(self):
        self.response = self.client.get(reverse('new_user_form'))
        self.assertTemplateUsed(self.response, template_name='signup.html')

    def test_submitting_valid_form_should_create_new_user(self):
        self.assertEquals(0, User.objects.count())
        form_data = {"email":"supermarket@email.com", "password1":"password", "password2":"password"}
        self._submit_form(reverse('create_user'), form_data)
        self.failUnless(User.objects.get(email="supermarket@email.com"))

    def test_submitting_form_with_mismatching_passwords_should_not_create_new_user(self):
        self.assertEquals(0, User.objects.count())
        form_data = {"email":"supermarket@email.com", "password1":"password", "password2":"password123"}
        self._submit_form(reverse('create_user'), form_data)
        self.failUnlessRaises(User.DoesNotExist)

    def test_submitting_form_without_password_should_create_new_user(self):
        self.assertEquals(0, User.objects.count())
        form_data = {"email":"supermarket@email.com"}
        self._submit_form(reverse('create_user'), form_data)
        self.failUnlessRaises(User.DoesNotExist)

    def test_submitting_valid_form_without_password2_should_not_create_user(self):
        self.assertEquals(0, User.objects.count())
        form_data = {"email":"supermarket@email.com","password1":"password"}
        self._submit_form(reverse('create_user'), form_data)
        self.failUnlessRaises(User.DoesNotExist)

    def test_submitting_valid_form_should_redirect_to_new_page(self):
        form_data = {"email":"supermarket@email.com","password1":"password", "password2":"password"}
        response = self._submit_form(reverse('create_user'), form_data)
        self.assertRedirects(response, reverse('users_success'))

    def _submit_form(self, url, form_data):
        response = self.client.post(url, data=form_data)
        return response







