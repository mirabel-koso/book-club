from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Category(models.Model):
    """docstring for Category"""

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    """docstring for Book"""

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

