
from django import template
from tree.models import MenuItem

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    try:
        menu = MenuItem.objects.filter(parent_menu__name=menu_name, parent_item=None)
        return render_menu(menu)
    except MenuItem.DoesNotExist:
        return ""

def render_menu(menu_items):
    html = '<ul>'
    for item in menu_items:
        html += f'<li>{item.name}</li>'
        if item.children.exists():
            html += '<ul>'
            html += render_menu(item.children.all())
            html += '</ul>'
    html += '</ul>'
    return html
