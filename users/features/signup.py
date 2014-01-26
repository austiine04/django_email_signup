from django.core.urlresolvers import reverse
from lettuce.django import django_url
from lettuce import step, world, before, after
from lettuce.django import django_url
from users.features.page_objects.signup_page import SignupPage


@step(u'Given I access the url "([^"]*)".')
def given_i_access_the_url_group1(step, url):
    world.page = SignupPage(world.browser, url)
    world.page.visit()

@step(u'And i sign up with credentials "([^"]*)", "([^"]*)", "([^"]*)".')
def and_i_sign_up_with_credentials(step, email, password1, password2):
    world.page.fill("email", email)
    world.page.fill("password1", password1)
    world.page.fill("password2", password2)
    world.page.click("btn_sign_up")

@step(u'Then i should not see "([^"]*)"')
def then_i_should_see(step, text):
    assert world.page.text_is_not_present(text), "Form submission failed"

@step(u'And i should see "([^"]*)"')
def and_i_should_see(step, text):
    assert world.page.is_text_present(text)