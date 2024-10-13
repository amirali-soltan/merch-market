from django.urls import path, include

app_name = 'app_payment'

urlpatterns = [
    path('api/', include('app_payment.api.urls')),
]