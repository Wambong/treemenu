from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'tree.html')

# views.py
from django.shortcuts import render
from .models import Menu
from .templatetags.menu_tag import render_menu

def get_menu_items(request, menu_name):
    menu = Menu.objects.get(name=menu_name)
    menu_items_html = render_menu(menu)
    return render(request, 'template.html', {'menu_name': menu_name, 'menu_items_html': menu_items_html})
