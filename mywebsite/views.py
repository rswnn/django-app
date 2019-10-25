from django.http import HttpResponse
from django.shortcuts import render

def index (request):
    return render(request, 'index.html')

def header (request):
    return render(request, 'header.html')

def menu (request):
    return render(request, 'menu.html')

def home (request):
    return render(request, 'home.html')

def footer (request):
    return render(request, 'footer.html')

def profil (request):
    return render(request, 'profil.html')
def gallery (request):
    return render(request, 'gallery.html')
def kontak (request):
    return render(request, 'kontak.html')