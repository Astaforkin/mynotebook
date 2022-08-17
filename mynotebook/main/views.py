from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h4>Проверка работы</h4>')    

def page(request):
    return HttpResponse('<h4>Страница блокнота</h4>')