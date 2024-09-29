from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Blog, Category, Tag, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class BlogAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ['show_image', 'title', 'author', 'categories_def', 'tags_def', 'status']
    list_filter = ['author', 'categories', 'tags', 'status']
    search_fields = ('title',)

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

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Comment)