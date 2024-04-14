from django.shortcuts import render,redirect
from .models import Shelf_Post
from .form import MusicForm


def shelfpage(request):
    posts=Shelf_Post.objects.all()
    return render(request,"music/shelfpage.html",{"posts":posts})

def upload_document(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')  # アップロード成功時のページにリダイレクト
    else:
        form = MusicForm()
    return render(request, 'music/addpage.html', {'form': form})