from django.http import *
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import SignUpForm
from myapp.models import WingmanUser

# Create your views here.
def user_signup(request):
	signup_form = SignUpForm()
	if request.method == 'POST':
		signup_form = SignUpForm(request.POST)
		if signup_form.is_valid():
			signup_form.save()
			username = signup_form.cleaned_data.get('username')
			raw_password = signup_form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			w = WingmanUser.objects.create(user=user, imagePath='myapp/images/profileImages/Barney.jpg')
			w.save()
			login(request, user)
			return redirect('/')
	signup_form = SignUpForm()
	return render(request, 'authentication/signup.html', {'signup_form':signup_form, 'show_login':False, 'login_errors':False})

def user_login(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    signup_form = SignUpForm()
    return render(request, 'authentication/signup.html', {'signup_form': signup_form, 'show_login':True, 'login_errors':True})

def logout_user(request):
	signup_form = SignUpForm()
	return render(request, 'authentication/signup.html', {'signup_form': signup_form, 'show_login':True, 'login_errors':False})


def logout_redirect(request):
	logout(request)
	return render(request, 'authentication/logout.html', context=None)
