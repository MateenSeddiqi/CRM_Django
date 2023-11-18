from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def landing(request):
    return render(request, 'landing.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # authenticate the user
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, " You have logged In")
            return redirect('home')
        else:
            messages.success(request, "Please Check Username or Password and try again")
            return redirect ('login_user')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You are logout ")
    return redirect (login_user)

def home(request):
    return render(request, 'home.html')



