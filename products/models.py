from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    image = models.ImageField(null=False)
    tag=models.CharField(max_length=200,null=True)
    description=models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image1 = models.ImageField(null=True)
    image2 = models.ImageField(null=True)
    price = models.PositiveIntegerField(default=0)
    price2 = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'
