

from django import template
from menu.models import Menu, Product
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def draw_menu():
    base_menus = Menu.objects.filter(parent=None)
    if not base_menus:
        return ''
    html = ''
    for base_menu in base_menus:
        html += draw_menu_recursive(base_menu)
    return mark_safe(html)

def draw_menu_recursive(menu):
    html = ''
    if menu.children.exists():
        # This menu item has children, so create a dropdown menu
        html += f'<li class="nav-item dropdown">'
        html += f'<a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">{menu.name}</a>'
        html += '<div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">'
        for child in menu.children.all():
            html += f'<a class="dropdown-item" href="{child.get_absolute_url()}">{child.name}</a>'
        html += '</div></li>'
    else:
        # This menu item does not have children, so just create a link
        html += f'<li class="nav-item"><a class="nav-link" href="{menu.get_absolute_url()}">{menu.name}</a></li>'
    return html
