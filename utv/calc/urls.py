from django.contrib import admin
from django.urls import path
from calc import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('project/', views.project)

]