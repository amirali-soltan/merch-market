from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app_payment.models import Basket, BasketItem
from app_payment.api.serializers import BasketSerializer
from app_market.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['GET'])
def basket_detail(request, id):
    book = Basket.objects.get(id=id)
    data = BasketSerializer(book).data
    return Response(data)


@api_view(['GET'])
def basket_list(request):
    basket_list = Basket.objects.all()
    data = BasketSerializer(basket_list, many=True).data
    return Response(data, status.HTTP_200_OK)


@api_view(['DELETE'])
def basket_delete(request):
    pk = request.POST.get('pk', None)
    if pk is not None:
        try:
            basket = Basket.objects.get(id=pk)
            basket.delete()
            return Response({'message': 'Deleted successfully!'}, status.HTTP_204_NO_CONTENT)
        except (ValueError, Basket.DoesNotExist) as err:
            return Response({'message': str(err)}, status.HTTP_400_BAD_REQUEST)
    return Response({'message': 'pk required!'}, status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def basket_create(request):
    user_id = request.data.get('user_id', None)
    product_id = request.data.get('product_id', None)
    count = request.data.get('count', None)
    user = User.objects.get(id=user_id)
    basket = Basket.objects.create(user=user)
    product = Product.objects.get(id=product_id)
    BasketItem.objects.create(basket=basket, product=product, count=count)
    
    return Response({'message': 'created successfully!'}, status.HTTP_201_CREATED)


@api_view(['PUT'])
def basket_update(request, id):
    product_id = request.data.get('product_id', None)
    count = request.data.get('count', None)

    try:
        basket = Basket.objects.get(id=id)
    except Basket.DoesNotExist:
        return Response({'message': 'Basket not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        basket_item = BasketItem.objects.get(basket=basket, product__id=product_id)
        basket_item.count = count
        basket_item.save()
        return Response({'message': 'updated successfully!'}, status=status.HTTP_200_OK)

    except Product.DoesNotExist:
        return Response({'message': 'Product not found in basket!'}, status=status.HTTP_404_NOT_FOUND)