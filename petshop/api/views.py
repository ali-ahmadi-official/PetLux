from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from blog.models import Blog, Category as BlogCategory, Tag as BlogTag, Comment as BlogComment
from product.models import Product, Category as productCategory, Tag as productTag, Comment as productComment
from .serializers import (
    BlogSerializer, BlogCategorySerializer, BlogTagSerializer, BlogCommentSerializer,
    ProductSerializer, ProductCategorySerializer, ProductCommentSerializer, ProductTagSerializer
)

class BlogsAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["categories", "author", "tags"]
    search_fields = ["title"]
    ordering_fields = ["created_at"]

class BlogAPIView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogCategoriesAPIView(generics.ListAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer

class BlogTagsAPIView(generics.ListAPIView):
    queryset = BlogTag.objects.all()
    serializer_class = BlogTagSerializer

class BlogCommentsAPIView(generics.ListAPIView):
    serializer_class = BlogCommentSerializer

    def get_queryset(self):
        blog_id = self.kwargs.get('pk')
        return BlogComment.objects.filter(blog=blog_id)

class ProductsAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["categories", "tags"]
    search_fields = ["name"]
    ordering_fields = ["created_at"]

class ProductAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCategoriesAPIView(generics.ListAPIView):
    queryset = productCategory.objects.all()
    serializer_class = ProductCategorySerializer

class ProductTagsAPIView(generics.ListAPIView):
    queryset = productTag.objects.all()
    serializer_class = ProductTagSerializer

class ProductCommentsAPIView(generics.ListAPIView):
    serializer_class = ProductCommentSerializer

    def get_queryset(self):
        product_id = self.kwargs.get('pk')
        return productComment.objects.filter(product=product_id)