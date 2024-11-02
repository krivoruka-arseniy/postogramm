from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import Users


class RegisterUser(UserCreationForm):
    class Meta:
        model = Users
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]