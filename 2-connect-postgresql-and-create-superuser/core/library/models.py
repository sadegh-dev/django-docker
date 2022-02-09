from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250)

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    name = models.CharField(max_length=250)
    pages = models.PositiveIntegerField()


