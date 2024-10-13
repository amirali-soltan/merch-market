from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from app_market.models import Product

User = get_user_model()

class Comment(models.Model):
    product = models.ForeignKey( Product , on_delete=models.CASCADE , null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    suggest = models.BooleanField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    positive_points = models.TextField(blank=True, null=True)
    negative_points = models.TextField(blank=True, null=True)
    helpful_count = models.PositiveIntegerField(default=0)
    not_helpful_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.product.name_fa}"
    
class Question(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='questions')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='answer')
    answer_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey("content_type", "object_id")
