from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import HttpResponse, Http404
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
# Create your views here.


class WomenHome(ListView):
    model = Women
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)

# def index(request):
#     post = Women.objects.all()
#     return render(request, 'index.html', {'title': 'Главная страница',
#                                           'posts': post,
#                                           'cat_selected': 0,
#                                           })


def about(request):
    return render(request, 'about.html', {'title': 'О сайте',
                                           })


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'addpage.html'
    success_url = reverse_lazy('home')

# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#
#     else:
#         form = AddPostForm()
#     return render(request, 'addpage.html', {'title': 'Добавление статьи',
#                                             'form': form,
#                                             })


def login(request):
    return HttpResponse('Войти')


def contact(request):
    return HttpResponse('Связаться с нами!')


class ShowPost(DetailView):
    model = Women
    template_name = 'post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'posts'
# def showpost(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#     return render(request, 'post.html', {'title': post.title,
#                                          'posts': post,
#                                          'cat_selected': post.cat_id,
#                                          })


class WomenCategory(ListView):
    model = Women
    template_name = 'index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['post_slug'], is_published=True)
# def show_category(request, post_slug):
#     cat = get_object_or_404(Category, slug=post_slug)
#     post = Women.objects.filter(cat=cat.pk)
#     return render(request, 'index.html', {'title': cat.name,
#                                           'posts': post,
#                                           'cat_selected': cat,
#                                           })
