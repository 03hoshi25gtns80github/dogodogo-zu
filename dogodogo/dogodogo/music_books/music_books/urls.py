from django.contrib import admin
from django.urls import path
from music_shelf.views import frontpage,signup

#受け渡し
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
]
