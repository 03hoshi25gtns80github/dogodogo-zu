from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )

# Create your models here.
class Todo(models.Model):
    url = models.CharField("URL", max_length=50)
    title = models.CharField("タイトル", max_length = 50)
    artist = models.CharField("アーティスト名", max_length = 50)

    def __str__(self):
        return self.title
