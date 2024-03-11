from django.contrib import admin
from blog.models import BlogPost, CategoryPost

# Register your models here.


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", 'published', 'created_on', 'last_update', 'author', )
    list_editable = ("published", )


@admin.register(CategoryPost)
class CategoryPostAdmin(admin.ModelAdmin):
    list_display = ("title", 'color', )
