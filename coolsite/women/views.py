from django.shortcuts import render
from .models import *
from django.http import HttpResponse, Http404
# Create your views here.
menu = [{'title':'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'addpage'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
        ]


def index(request):
    post = Women.objects.all()
    return render(request, 'index.html', {'title': 'Главная страница',
                                          'menu': menu,
                                          'posts': post,
                                          'cat_selected': 0,
                                          })


def about(request):
    return render(request, 'about.html', {'title': 'О сайте',
                                          'menu': menu
                                           })

def addpage(request):
    return HttpResponse('Добавить страницу')


def login(request):
    return HttpResponse('Войти')


def contact(request):
    return HttpResponse('Связаться с нами!')


def showpost(request, post_id):
    return HttpResponse(f'Выведи пост с id = {post_id}!')


def show_category(request, cat_id):
    post = Women.objects.filter(cat_id=cat_id)
    if  len(post) == 0:
        raise Http404()
    return render(request, 'index.html', {'title': 'Отоброжение по рубрикам',
                                          'menu': menu,
                                          'posts': post,
                                          'cat_selected': cat_id,
                                          })
