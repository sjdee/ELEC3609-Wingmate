from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, WingmanUser
from signup.forms import SignUpForm

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        print("authenticated")
        return render(request, 'myapp/index.html', context=None)
    else:
        print("NOT authenticated")
        return render(request, 'myapp/welcome.html', context=None)

def contact(request):
    return render(request, 'myapp/contact.html', context=None)

def about(request):
    return render(request, 'myapp/about.html', context=None)

def posts(request):
    posts = Post.objects.all()
    return render(request, 'myapp/posts.html', context=None)

def profile(request):
	user = request.user # This is the current user that has logged in.s
	currentUser = WingmanUser.objects.get(user=user) # This is the current WingmanUser. Each user is related to a wingmanuser.
	# print(test.imagePath)
	return render(request, 'myapp/profile.html', {'user': currentUser})
