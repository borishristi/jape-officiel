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
    context = {"post": post, "post_1": post_1, "post_2": post_2, "post_3": post_3, "posts": posts}
    return render(request, "blog/posts_list.html", context)


def image_view(request):
    return render(request, "blog/article_01.html")
