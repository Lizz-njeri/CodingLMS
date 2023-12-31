from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.conf import settings

class UserCreateForm(UserCreationForm):
    phone = forms.CharField(max_length=15, required=False, help_text="Enter your phone number.")

    class Meta:
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2', 'user_type')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['email'].label = "Email Address"
        self.fields['phone'].label = "Phone Number"
        self.fields['user_type'].label = "Register as:"