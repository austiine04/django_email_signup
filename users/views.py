from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from users.forms import SignupForm
from users.models import User


class SignUpView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'signup.html'
    context_object_name = 'form'
    success_url = reverse_lazy('users_success')
