from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('addpage/', views.addpage, name='addpage'),
    path('login/', views.login, name='login'),
    path('post/<int:post_id>', views.showpost, name='post'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
]