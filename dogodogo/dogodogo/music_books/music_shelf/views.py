from http.client import HTTPResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

def frontpage(request):
    return render(request, "music/frontpage.html")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('frontpage')
    else:
        form = SignUpForm()
    return render(request, 'music/signup.html', {'form': form})

def user_login(request):  # Changed from def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('login_success')  # Changed from return redirect('frontpage')
    else:
        form = AuthenticationForm()
    return render(request, 'music/login.html', {'form': form})

def login_success(request):
    return render(request, 'music/login_success.html')