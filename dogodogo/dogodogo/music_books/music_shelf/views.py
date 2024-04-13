from http.client import HTTPResponse
from django.shortcuts import render

def frontpage(request):
    return render(request, "music/frontpage.html")
