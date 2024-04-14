from django.contrib import admin
from django.urls import path, include
from music_shelf.views import frontpage,signup, user_login, login_success, user_page, TodoDetail, TodoList, TodoCreate, TodoUpdate, TodoDelete
from music_shelf.views import shelfpage,upload_document

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',upload_document),
    path('shelf/',shelfpage)
    path("", frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('login_success/', login_success, name='login_success'),
    path('user/<str:username>/', user_page, name='user_page'),
    path("shelf/", TodoList.as_view(), name="list"),
    path("detail/<int:pk>", TodoDetail.as_view(), name="detail"),
    path("create/", TodoCreate.as_view(), name="create"),
    path("update/<int:pk>", TodoUpdate.as_view(), name="update"),
    path("delete/<int:pk>", TodoDelete.as_view(), name="delete"),
    #path("", include("music_shelf.urls")) 
]