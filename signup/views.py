from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from authentication.forms import SignUpForm
from django.contrib.auth import logout

from myapp.models import WingmanUser

# Create your views here.
####	commented but need the line about the WingmanUser  ####	
# def register(request):
# 	if request.method == 'POST':
# 		form = SignUpForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			username = form.cleaned_data.get('username')
# 			print(form.cleaned_data.get('first_name'))
# 			raw_password = form.cleaned_data.get('password1')
#
# 			user = authenticate(username=username, password=raw_password)
# 			w = WingmanUser.create(user=user, imagePath='myapp/images/profileImages/Barney.jpg')
# 			w.save()
# 			login(request, user)
# 			return redirect('/')
# 	else:
# 		form = SignUpForm()
#
# 	return render(request, 'signup/register.html', {'form': form})


def logout_redirect(request):
	logout(request)
	return render(request, 'authentication/logout.html', context=None)
