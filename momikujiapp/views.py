from random import randint
from django.shortcuts import render
from django.http import HttpResponse
from .models import MomikujiModel

# Create your views here.

def momikuji(request):
    return render(request, 'momikujiapp/momikuji.html')

def draw(request):
    count = len(MomikujiModel.objects.all())
    rand_id = randint(1, count)
    momikuji = MomikujiModel.objects.get(pk=rand_id)
    return render(request, 'momikujiapp/result.html', {'momikuji': momikuji})