from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-input'

        # set placeholders
        self.fields['first_name'].widget.attrs['placeholder'] = 'first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'last name'
        self.fields['email'].widget.attrs['placeholder'] = 'your email address'
        self.fields['username'].widget.attrs['placeholder'] = 'your username'
        self.fields['password1'].widget.attrs['placeholder'] = 'choose a password'
        self.fields['password2'].widget.attrs['placeholder'] = 'confirm your password'

        # other
        self.fields['last_name'].widget.attrs['style'] = 'float: right;'

        for field in self.fields:
            self.fields[field].help_text=""
