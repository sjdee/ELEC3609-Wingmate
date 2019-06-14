from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Handles Wingman user signups and stores their data in a User
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, required=True)

	#meta attribute class with user details, uses the default User as the model and specifies the fields
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
    	super(UserCreationForm, self).__init__(*args, **kwargs)

    	for field in self.fields:
    		self.fields[field].help_text=""
