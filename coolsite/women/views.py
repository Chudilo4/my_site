from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import HttpResponse, Http404
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class WomenHome(DataMixin, ListView):
    paginate_by = 3
    model = Women
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items())+list(c_def.items()))

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


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items())+list(c_def.items()))



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


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

def login(request):
    return HttpResponse('Войти')


def contact(request):
    return HttpResponse('Связаться с нами!')


class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['posts'])
        return dict(list(context.items())+list(c_def.items()))
# def showpost(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#     return render(request, 'post.html', {'title': post.title,
#                                          'posts': post,
#                                          'cat_selected': post.cat_id,
#                                          })


class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'index.html'
    context_object_name = 'posts'
    allow_empty = False

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Категория - ' + str(context['posts'][0].cat)
    #     context['cat_selected'] = context['posts'][0].cat_id
    #     return context
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['post_slug'], is_published=True)
# def show_category(request, post_slug):
#     cat = get_object_or_404(Category, slug=post_slug)
#     post = Women.objects.filter(cat=cat.pk)
#     return render(request, 'index.html', {'title': cat.name,
#                                           'posts': post,
#                                           'cat_selected': cat,
#                                           })
