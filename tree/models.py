# menu_app/models.py
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    parent_menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    parent_item = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

