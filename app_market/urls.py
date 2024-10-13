

from django.urls import path
from .views import index,my_search,product_detail,blog,blog_detail,product_comment,product_list_by_category,faq

app_name = 'app_market'

urlpatterns = [
    path('',index,name='home'),
    path('search/', my_search, name='search'),
    path('product/<int:id>/', product_detail, name='product_detail'),
    path('product/<int:id>/comment/', product_comment, name='p_comment'),
    path('blog/', blog , name='blog' ),
    path('blog/detail/', blog_detail , name='blogdetail' ),
    path('products/category/<int:category_id>/', product_list_by_category, name='product_list_by_category'),
    path('faq/', faq, name='faq'),

]
