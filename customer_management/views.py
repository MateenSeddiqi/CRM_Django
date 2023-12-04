from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
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
    return redirect ('login_user')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You are Signup ")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form':form})
    return render(request, 'signup.html', {'form':form})


def home(request):
    records= Record.objects.all()
    return render(request, 'home.html', {'records':records})


def show_record(request, pk):
    if request.user.is_authenticated:
        show_record = Record.objects.get(id=pk)
        return render (request, 'show_record.html', {'show_record':show_record})
    else:
        messages.success(request, " You must be login ")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "data deleted ")
        return redirect ('home')
    else:
        messages.success(request, "You must be login ")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record added")
                return redirect ('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You Must login ")
        return redirect('login_user')
