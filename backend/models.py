from django.db import models


class Shop(models.Model):
    name = models.CharField()
    url = models.CharField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField()
    shops = models.ManyToManyField(Shop, related_name='categories')


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=True)
    name = models.CharField()


class ProductInfo(models.Model):
    product = models.ForeignKey(Product, on_delete=True)
    shop = models.ForeignKey(Shop, on_delete=True)
    name = models.CharField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    price_rrc = models.IntegerField()


class Parameter(models.Model):
    name = models.CharField()


class ProductParameter(models.Model):
    product_info = models.ForeignKey(ProductInfo, on_delete=True)
    parameter = models.ForeignKey(Parameter, on_delete=True)
    value = models.IntegerField()


class Order(models.Model):
    user = models.IntegerField()
    dt = models.DateField()
    status = models.BooleanField()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=True)
    pruduct = models.ForeignKey(Product, on_delete=True)
    shop = models.ForeignKey(Product, on_delete=True)
    quantity = models.IntegerField()


class Contact(models.Model):
    type = models.CharField
    user = models.IntegerField
    value = models.CharField