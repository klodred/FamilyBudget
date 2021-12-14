from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, redirect

menu = ["Войти", "Регистрация"]

def index(request):
    #return HttpResponse(request, 'menu/index.html')
    return render(request, 'menu/index.html', {'title': 'Главная страница', 'menu': menu})

def login(request):
    return HttpResponse("Войти")

def signin(request):
    return HttpResponse("Регистрация")