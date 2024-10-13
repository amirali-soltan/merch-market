from django.urls import path, include
from app_payment.api import views

urlpatterns = [
    path('basket/<int:id>/', views.basket_detail, name='api-basket'),
    path('basket/list/', views.basket_list),
    path('basket/delete/', views.basket_delete, name='api-basket-delete'),
    path('basket/create/', views.basket_create, name='api-basket-create'),
    path('basket/update/<int:id>/', views.basket_update, name='api-basket-update'),
]