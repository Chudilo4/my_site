from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.WomenHome.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('addpage/', views.AddPage.as_view(), name='addpage'),
    path('login/', views.login, name='login'),
    path('register', views.RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>', views.ShowPost.as_view(), name='post'),
    path('category/<slug:post_slug>/', views.WomenCategory.as_view(), name='category'),
]
