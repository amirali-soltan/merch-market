from rest_framework import serializers
from app_payment.models import Basket, BasketItem
from app_market.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializr(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    def get_category(self, obj):
        return CategorySerializer(obj.Category.all(), many=True).data

    class Meta:
        model = Product
        fields = [
            'id',
            'name_fa',
            'name_en',
            'price',
            'count',
            'brand',
            'is_suggested',
            'category',
        ]


class BasketItemSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()

    def get_product(self, obj):
        return ProductSerializr(obj.product).data

    class Meta:
        model = BasketItem
        fields = ['id', 'count', 'product']

class BasketSerializer(serializers.ModelSerializer):
    basket_item = serializers.SerializerMethodField()

    def get_basket_item(self, obj):
        basket_items = obj.basketitem_set.all()
        return BasketItemSerializer(basket_items, many=True).data

    class Meta:
        model = Basket
        fields = '__all__'