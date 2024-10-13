from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse

User = get_user_model()

class Product(models.Model):
    name_fa = models.CharField(max_length=255, null=True)
    name_en = models.CharField(max_length=255, null=True)
    price = models.PositiveIntegerField()
    discount = models.IntegerField(default=0)
    count = models.PositiveIntegerField()
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    is_suggested = models.BooleanField(default=False)
    is_amazing = models.BooleanField(default=False)
    footer_right = models.BooleanField(default=False)
    footer_left = models.BooleanField(default=False)
    footer_Middle = models.BooleanField(default=False)
    Category = models.ManyToManyField('Category')
    color = models.ManyToManyField('color')
    features = models.ManyToManyField('features')

    @property
    def images(self):
        return Image.objects.filter(
            object_id=self.id,
            content_type=ContentType.objects.get_for_model(self.__class__).id
        )

    def get_absolute_url(self):
        return reverse('app_market:product_detail', args=(self.id, ))

    def discounted_price(self):
        if self.discount > 0:
            return self.price - (self.price * self.discount // 100)
        return self.price
    
    def __str__(self):
        return self.name_fa or ''

class Color(models.Model):
    color = models.CharField(max_length=255)
    hex_code = models.CharField(max_length=35,null=True)

    def __str__(self):
        return self.color

class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Banner(models.Model):
    title = models.CharField(max_length=255)

    @property
    def images(self):
        return Image.objects.filter(
            object_id=self.id,
            content_type=ContentType.objects.get_for_model(self.__class__).id
        )

    def __str__(self):
        return self.title

class Category(models.Model):
    parent = models.ForeignKey( 'self', related_name='sub_categories', on_delete=models.SET_NULL, null=True, blank=True )
    name = models.CharField(max_length=50 , null=True)
    slug = models.SlugField(max_length=50 , null=True , blank=True)
    is_available = models.BooleanField(default= True)

    def __str__(self):
        return self.name
    
class features(models.Model):
    text = models.CharField(max_length=255)
    answer = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.text
    
class review(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='review' , null=True)
    description = models.TextField(blank=True , null=True)

class special_feature(models.Model):
    text = models.CharField(max_length=255,null=True)
    main_text = models.TextField(null=True)
    review = models.ForeignKey("review", on_delete=models.CASCADE , related_name='feature' , null=True)

    def __str__(self):
        return self.text

class ProductDescription(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='descriptions')
    title = models.CharField(max_length=100 , blank=True , null=True)
    description = models.TextField( blank=True , null=True )

    def __str__(self):
        return self.title
    
class Blog(models.Model):
    title = models.CharField(max_length=255)

    @property
    def images(self):
        return Image.objects.filter(
            object_id=self.id,
            content_type=ContentType.objects.get_for_model(self.__class__).id
        )

    def __str__(self):
        return self.title
    
class Blog_detail(models.Model):
    title = models.CharField( max_length=150 , blank=True , null=True)
    description= models.TextField()

    @property
    def images(self):
        return Image.objects.filter(
            object_id=self.id,
            content_type=ContentType.objects.get_for_model(self.__class__).id
        )

    def __str__(self):
        return self.title
    
class Image(models.Model):
    url = models.CharField(max_length=150, null=True, blank=True)
    image = models.ImageField(upload_to='store/images/', null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, related_name='app_market_images')
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.image.url
    
