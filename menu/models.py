from django.db import models
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

class Menu(models.Model):
    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        unique_together = [['parent', 'slug', ]]
        verbose_name = 'menu'
        verbose_name_plural = 'menus'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return '/%s/' % (self.slug)
    def clean(self):
        if self.parent == self:
            raise ValidationError("A menu cannot be a child of itself.")
        super().clean()
    def get_menu_path(self):
        menu_path = ['<a href="{}">{}</a>'.format(self.get_absolute_url(), self.name)]
        current_menu = self.parent
        while current_menu:
            menu_path.insert(0, '<a href="{}">{}</a>'.format(current_menu.get_absolute_url(), current_menu.name))
            current_menu = current_menu.parent
        return ' / '.join(menu_path)

class Product(models.Model):
    name = models.CharField(max_length=100)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, blank=True, related_name='products')
    images = models.ImageField(upload_to='photos/products', null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    def get_url(self):
        return self.slug
    def __str__(self):
        return self.name
