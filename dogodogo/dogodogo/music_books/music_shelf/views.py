from http.client import HTTPResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo, User
from django.contrib.auth.models import User 


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
            return redirect('user_page', username=user.username)  # Redirect to user-specific page
    else:
        form = AuthenticationForm()
    return render(request, 'music/login.html', {'form': form})

def login_success(request):
    return render(request, 'music/login_success.html')

def user_page(request, username):
    return render(request, 'music/user_page.html', {'username': username})


class UserSearch(ListView):
    model = User
    template_name = 'music_shelf/user_search.html'

    def get_queryset(self):
        # 検索フォームが送信されたときに前回の検索結果をクリアする
        self.object_list = None
        query = super().get_queryset()
        title = self.request.GET.get('title', None)
        if title:
            query = query.filter(username__icontains=title)
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.request.GET.get('title', '')
        return context

class TodoList(ListView):
    model = Todo
    context_object_name = "tasks"


class TodoDetail(DetailView):
    model = Todo
    context_object_name = "task"

class TodoCreate(CreateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("list")

class TodoUpdate(UpdateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("list")

class TodoDelete(DeleteView):
    model = Todo
    context_object_name = "task"
    success_url = reverse_lazy("list")