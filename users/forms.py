from django.contrib.auth.forms import UserCreationForm
from users.models import User


class SignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        del self.fields['username']

    class Meta:
        model = User
        fields = ('email',)


