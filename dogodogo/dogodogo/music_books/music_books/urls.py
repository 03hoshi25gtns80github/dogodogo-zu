from django.contrib import admin
from django.urls import path
from music_shelf.views import frontpage

#受け渡し
urlpatterns = [
    path('admin/', admin.site.urls),
]
