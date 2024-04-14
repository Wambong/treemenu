from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('get-menu-items/<str:menu_name>/', views.get_menu_items, name='menu_items'),

]