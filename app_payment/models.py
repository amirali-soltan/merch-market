from django.db import models
from app_market.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()

TRANSACTION_CHOICES = (
    (False, 'Faile'),
    (True, 'Success'),
)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction = models.OneToOneField('Transaction', on_delete=models.CASCADE)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()

class Transaction(models.Model):
    status = models.BooleanField(default=False, choices=TRANSACTION_CHOICES)
    ref_code = models.CharField(max_length=255)
    price = models.IntegerField()