from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def momikuji(request):
    response = HttpResponse('hello, world!')
    return response