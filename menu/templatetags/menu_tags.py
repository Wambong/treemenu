from django import template
from menu.models import Menu, Product
from django.urls import reverse
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    base_menu = Menu.objects.filter(name=menu_name).first()
    if not base_menu:
        return ''
    html = ''
    html += draw_menu_recursive(base_menu)
    return mark_safe(html)

def draw_menu_recursive(menu):
    html = ''
    html += '<ul>'
    html += f'<li><a href="{reverse("menu_detail", args=[menu.slug])}">{menu.name}</a></li>'
    for child in menu.children.all():
        html += draw_menu_recursive(child)
    html += '</ul>'
    return html
