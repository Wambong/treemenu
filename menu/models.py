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
class Product(models.Model):
    name = models.CharField(max_length=100)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, blank=True, related_name='products')
    images = models.ImageField(upload_to='photos/products', null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    def get_url(self):
        return self.slug
    def __str__(self):
        return self.name
