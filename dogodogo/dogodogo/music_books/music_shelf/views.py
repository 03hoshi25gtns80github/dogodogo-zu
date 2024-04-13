from http.client import HTTPResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import SignUpForm
from django.contrib.auth import login, authenticate

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