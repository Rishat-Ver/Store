from django.db import models
from django.db.models import (CharField, DateTimeField, DecimalField,
                              ForeignKey, ImageField, PositiveIntegerField,
                              TextField)

from users.models import User


class ProductCategory(models.Model):
    name = CharField(max_length=128, unique=True)
    description = TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = CharField(max_length=256)
    description = TextField()
    price = DecimalField(max_digits=7, decimal_places=2)
    quantity = PositiveIntegerField(default=0)
    image = ImageField(upload_to='products_image')
    category = ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f' Продукт: {self.name} | Категория: {self.category.name}'


class BasketQuantity(models.QuerySet):

    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = ForeignKey(to=User, on_delete=models.CASCADE)
    product = ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = PositiveIntegerField(default=0)
    created_timestamp = DateTimeField(auto_now_add=True)
    objects = BasketQuantity.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт: {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity
