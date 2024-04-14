from django.contrib import admin
from .models import Menu
from .models import MenuItem
# Register your models here.

admin.site.register(MenuItem)
admin.site.register(Menu)
