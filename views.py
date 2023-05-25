from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from . models import team


# Create your views here.

def home3(request):
    obj = Place.objects.all()
    object = team.objects.all()
    return render(request, "index.html", {'result': obj, 'result1': object})


def aboutfun(request):
    name = "home"
    return render(request, 'index4.html', {'obj': name})


def contactfun(request):
    return HttpResponse("<h1>contact Page</h1>")


def addition(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    res = x + y
    return render(request, "result.html", {'result': res})
