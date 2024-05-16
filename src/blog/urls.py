from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from jape_officiel import settings
from .views import base_view, image_view, home_view, post_view, posts_view, category_post_view, about_view, \
    contact_view, blog_view
from .views import index_view, category2_view, contact2_view, single_view, save_comment, tag_view

urlpatterns = [
    path('', index_view, name="index"),
    path('home/', home_view, name="home_view"),
    path('category/<str:category>/', category2_view, name="categorie"),
    path('tag/<str:tag>/', tag_view, name="tag"),
    path('contact/', contact2_view, name="contact"),
    path('blog/', blog_view, name="blog"),
    path('save_comment/', save_comment, name="save_comment"),
    path('single/<str:slug>', single_view, name="single"),
    # path('index/', index_view, name="index"),

    # path('base/', base_view, name="base_view"),
    # path('posts/', posts_view, name="posts_view"),
    # path('about/', about_view, name="about_view"),
    # path('contact/', contact_view, name="contact_view"),
    # path('category/<str:category>/', category_post_view, name="category"),
    # path('post/<str:slug>/', post_view, name="post_view"),
    # path('1/', image_view, name="image_view"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
