from django.contrib import admin
from django.utils.safestring import mark_safe
from product.models import Product, ProductType, Category, Tag, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ['show_image', 'name', 'categories_def', 'tags_def', 'price', 'is_free', 'is_available', 'status']
    list_filter = ['product_type', 'categories', 'tags', 'is_free', 'is_available', 'status']
    search_fields = ('name',)

    def categories_def(self, obj):
        return ", ".join(category.name for category in obj.categories.all())
    
    def tags_def(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())
    
    def show_image(self, obj):
        return mark_safe(f'<img src="{obj.cover.url}" style="width: 150px; height: auto; border-radius: 10px;" />')

    show_image.short_description = 'cover'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']
    list_filter = ['parent']

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Comment)