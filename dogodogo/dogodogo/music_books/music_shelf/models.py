from django.db import models

# Create your models here.
class Todo(models.Model):
    url = models.CharField("URL", max_length=50)
    title = models.CharField("タイトル", max_length = 50)
    artist = models.CharField("アーティスト名", max_length = 50)

    def __str__(self):
        return self.title