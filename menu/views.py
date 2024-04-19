from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Menu, Product

def home(request):
    return render(request, 'index.html')

def menu_detail(request, slug):
    menu = get_object_or_404(Menu, slug=slug)
    products = Product.objects.filter(menu=menu)
    return render(request, 'menu_detail.html', {'menu': menu, 'products': products})

