from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'title': 'Главная страница',
        'values':['Some','Hello']
    }
    return render(request, 'main/index.html', data)    

def page(request):
    return render(request, 'main/page.html')