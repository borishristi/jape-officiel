from django.contrib import admin
from blog.models import BlogPost, CategoryPost, CommentsPost, TagPost


# Register your models here.


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", 'published', 'created_on', 'last_update', 'author', )
    list_editable = ("published", )


@admin.register(CategoryPost)
class CategoryPostAdmin(admin.ModelAdmin):
    list_display = ("title", 'color', )


@admin.register(CommentsPost)
class CommentsPostAdmin(admin.ModelAdmin):
    list_display = ("comment", "author", "created_on", "last_update", "post", )


@admin.register(TagPost)
class TagPostAdmin(admin.ModelAdmin):
    list_display = ("title", "tag_slug", )
