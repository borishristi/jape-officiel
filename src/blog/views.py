from django.shortcuts import render

# Create your views here.
from blog.models import BlogPost


def base_view(request):
    return render(request, "base.html")
    # return HttpResponse("<h1>Ok c'est bon!!!</h1>")


def home_view(request):
    post = BlogPost.objects.first()
    posts = BlogPost.objects.all().filter(published=True)

    print(posts[0].title)
    print(posts[2].title)
    post_1 = posts[1]
    post_2 = posts[2]
    post_3 = posts[3]
    context = {"post": post, "post_1": post_1, "post_2": post_2, "post_3": post_3, "posts": posts[4:10], "r_posts": posts[:4]}
    return render(request, "blog/home_view.html", context)


def image_view(request):
    return render(request, "blog/article_01.html")


def post_view(request, slug):
    post = BlogPost.objects.get(slug=slug)
    return render(request, "blog/post_view.html", context={"post": post})


def posts_view(request):
    posts = BlogPost.objects.all().filter(published=True)
    return render(request, "blog/posts_view.html", {"posts": posts, "categories": posts[:4], "r_posts": posts[5:9]})
