from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from app_market.models import Product, Color, Brand, Banner, Image, Category, features, review, ProductDescription,special_feature,Blog,Blog_detail


class ImageInline(GenericStackedInline):
    model = Image
    extra = 1

class special_featureInline(admin.StackedInline):
    model = special_feature
    extra = 1

class reviewInline(admin.StackedInline):
    model = review
    extra = 1

class ProductDescriptionInline(admin.StackedInline):
    model = ProductDescription
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline , reviewInline ,ProductDescriptionInline ]

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
 
@admin.register(features)
class featuresAdmin(admin.ModelAdmin):
    pass

@admin.register(review)
class reviewAdmin(admin.ModelAdmin):
    inlines = [special_featureInline]
    pass

@admin.register(special_feature)
class special_featureAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductDescription)
class ProductDescriptionAdmin(admin.ModelAdmin):
    pass

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    pass

@admin.register(Blog_detail)
class Blog_detailAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    pass