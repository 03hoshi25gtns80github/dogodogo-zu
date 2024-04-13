from django.contrib import admin
from django.urls import path
from music_shelf.views import frontpage,signup, user_login, login_success, user_page

#受け渡し
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('login_success/', login_success, name='login_success'),
    path('user/<str:username>/', user_page, name='user_page'),
]
