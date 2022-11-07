from django.shortcuts import render
from .models import *
# Create your views here.
menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def index(request):
    post = Women.objects.all()
    return render(request, 'index.html', {'title': 'Главная страница',
                                          'menu': menu,
                                          'post': post
                                          })


def about(request):
    return  render(request, 'about.html', {'title': 'О сайте',
                                          'menu': menu
                                           })

