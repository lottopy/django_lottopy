# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def base(request):
    return render(request, 'lottopy/base.html',
    {'nbar': 'home'})

def home(request):
    return render(request, 'lottopy/home.html',
    {'nbar': 'home'})

def about(request):
    return render(request, 'lottopy/about.html',
    {'nbar': 'about', 'title': 'About'})
