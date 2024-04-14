from django.db import models

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
    
