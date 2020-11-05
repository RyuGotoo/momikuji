from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def momikuji(request):
    return render(request, 'momikujiapp/momikuji.html')