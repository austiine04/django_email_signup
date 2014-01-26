from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from users.views import SignUpView

urlpatterns = patterns('',
   url(r'^$',           SignUpView.as_view(), name='create_user'),
   url(r'^new/$',       SignUpView.as_view(), name='new_user_form'),
   url(r'^success/$',    TemplateView.as_view(template_name='users_success.html'), name='users_success'),
)

