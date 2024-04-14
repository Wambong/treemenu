from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('<slug:slug>/', views.menu_detail, name='menu_detail'),

]