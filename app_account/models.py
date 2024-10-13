from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=255)
    national_id = models.CharField(max_length=255,blank=True)
    image = models.ImageField(upload_to='store/images/', null=True)

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    postal_code = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
