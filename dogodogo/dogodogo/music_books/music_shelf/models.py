from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )

class Shelf_Post(models.Model):
    slug=models.SlugField()
    name=models.CharField(max_length=255)
    music_title=models.CharField(max_length=255)
    music_picture=models.ImageField()
    music_url=models.URLField()
    posted_date=models.DateTimeField(auto_now_add=True)
    
class Upload(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    music_url=models.URLField() 
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
class Todo(models.Model):
    url = models.CharField("URL", max_length=50)
    title = models.CharField("タイトル", max_length = 50)
    artist = models.CharField("アーティスト名", max_length = 50)

    def __str__(self):
        return self.title
