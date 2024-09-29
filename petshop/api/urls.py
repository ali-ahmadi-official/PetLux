from django.urls import path
from .views import *

urlpatterns = [
    path('blogs/', BlogsAPIView.as_view(), name='blogs_api'),
    path('blogs/<int:pk>/', BlogAPIView.as_view(), name='blog_api'),
    path('blog-categories/', BlogCategoriesAPIView.as_view(), name='blog_categories'),
    path('blog-tags/', BlogTagsAPIView.as_view(), name='blog_tags'),
    path('blogs/<int:pk>/comments/', BlogCommentsAPIView.as_view(), name='blog_comments'),
    path('products/', ProductsAPIView.as_view(), name='products_api'),
    path('products/<int:pk>/', ProductAPIView.as_view(), name='product_api'),
    path('product-categories/', ProductCategoriesAPIView.as_view(), name='product_categories'),
    path('product-tags/', ProductTagsAPIView.as_view(), name='product_tags'),
    path('products/<int:pk>/comments/', ProductCommentsAPIView.as_view(), name='product_comments'),
]