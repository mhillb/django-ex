import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
#from .models import PageView

# Create your views here.

def index(request):
    """Takes an request object as a parameter and creates an pageview object then responds by rendering the index view."""
    return render(request, 'welcome/index.html')

def retrieve(request):
    html = "<html><head><title></title></head><body>Testing ... ABC abc 123...</body></html>"
    return HttpResponse(html)

def health(request):
    """Takes an request as a parameter and gives the count of pageview objects as reponse"""
    return HttpResponse("")
