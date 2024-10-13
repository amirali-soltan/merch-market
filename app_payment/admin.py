from django.contrib import admin
from app_payment.models import  Order, OrderItem, Basket, BasketItem, Transaction


class BasketItemInline(admin.StackedInline):
    model = BasketItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
     inlines = [BasketItemInline]

@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass
