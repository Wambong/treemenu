from django import template
from menu.models import Product

register = template.Library()
@register.simple_tag
def draw_menu(menu_name):
    try:
        menu = Product.objects.get(name=menu_name)
        return render_menu(menu)
    except Product.DoesNotExist:
        return ""

def render_menu(menu):
    html = '<ul>'
    for item in menu.children.all():
        html += f'<li>{item.name}</li>'
        if item.children.exists():
            html += render_menu(item)
    html += '</ul>'
    return html
