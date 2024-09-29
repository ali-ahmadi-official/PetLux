from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from account.models import User

class ProductType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='subcategories', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('rejected', 'Rejected'),
    ]

    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='product_type_products')
    categories = models.ManyToManyField(Category, related_name="categories_blog")
    tags = models.ManyToManyField(Tag, related_name="tags_blog")
    cover = models.ImageField(default='defaults/product-1.jpg', upload_to='product/')
    name = models.CharField(max_length=100)
    description = CKEditor5Field('body', config_name='extends')
    is_available = models.BooleanField(default=True)
    is_free = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def save(self, *args, **kwargs):
        if self.is_free or self.is_available == False:
            self.price = 0
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Comment(models.Model):
    STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('rejected', 'Rejected'),
    ]

    product = models.ForeignKey(Product, related_name='product_comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_comment_product")
    text = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment by {self.author} on {self.product}'