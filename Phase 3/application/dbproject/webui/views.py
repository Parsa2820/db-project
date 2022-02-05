from django.shortcuts import render
from django.http import HttpResponse
from matplotlib.style import context

def home(request):
    context = {
    }
    return render(request, 'webui/home.html', context)

def about(request):
    return render(request, 'webui/about.html')
