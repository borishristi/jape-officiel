from django.shortcuts import render

# Create your views here.
from blog.models import BlogPost, CategoryPost, CommentsPost


def base_view(request):
    return render(request, "base.html")
    # return HttpResponse("<h1>Ok c'est bon!!!</h1>")


def home_view(request):
    post = BlogPost.objects.first()
    posts = BlogPost.objects.all().filter(published=True)

    categories = CategoryPost.objects.all()

    print(posts[0].title)
    print(posts[2].title)
    post_1 = posts[1]
    post_2 = posts[2]
    post_3 = posts[3]
    context = {"post": post, "post_1": post_1, "post_2": post_2, "post_3": post_3, "posts": posts[4:10],
               "r_posts": posts[:4], "categories": categories}
    return render(request, "blog/home_view.html", context)


def index_view(request):
    # select the first post
    i_post = BlogPost.objects.first()

    # select the all published posts
    i_posts = BlogPost.objects.all().filter(published=True)

    # randomly select 4 posts from the database, starting with post 4
    random_posts = BlogPost.objects.all().filter(published=True)[3:7]
    featured_posts = BlogPost.objects.all().filter(published=True)[7:12]

    # category post select
    categories = CategoryPost.objects.all()
    cat_1 = categories[1]
    cat_2 = categories[2]
    cat_3 = categories[3]
    cat_4 = categories[4]

    # posts = BlogPost.objects.all().filter(published=True, category=category_post)
    # category_post = CategoryPost.objects.get(cat_slug=category)

    category_posts_1 = BlogPost.objects.all().filter(published=True, category=cat_1)
    category_posts_2 = BlogPost.objects.all().filter(published=True, category=cat_2)
    category_posts_3 = BlogPost.objects.all().filter(published=True, category=cat_3)
    category_posts_4 = BlogPost.objects.all().filter(published=True, category=cat_4)

    # print("*******" * 5)
    # print(category_posts_1)
    # print("*******" * 5)
    # print(category_posts_2)
    # print("*******" * 5)
    # print(category_posts_3)
    # print("*******" * 5)
    # print(category_posts_4)

    # print(i_posts[0].title)
    # print(i_posts[2].title)

    i_post_1 = i_posts[0]
    i_post_2 = i_posts[1]
    i_post_3 = i_posts[2]
    context = {"post": i_post, "post_1": i_post_1, "post_2": i_post_2, "post_3": i_post_3, "posts": i_posts[4:10],
               "r_posts": i_posts[:4], "categories": categories, "random_posts": random_posts,
               "featured_posts": featured_posts, "cat_1": cat_1, "cat_2": cat_2, "cat_3": cat_3, "cat_4": cat_4,
               "categories_1": category_posts_1[:3], "categories_2": category_posts_2, "categories_3": category_posts_3,
               "categories_4": category_posts_4}
    return render(request, "blog/index.html", context)


def category2_view(request):
    return render(request, "blog/category.html")


def contact2_view(request):
    return render(request, "blog/contact.html")


def single_view(request, slug):
    single_post = BlogPost.objects.get(slug=slug)
    categories_post = single_post.category.all()
    posts = BlogPost.objects.all().filter(published=True).exclude(slug=single_post.slug)
    categories = CategoryPost.objects.all()
    comments = CommentsPost.objects.all().filter(post=single_post)

    print("*******" * 5)
    print(single_post.slug)
    print("*******" * 5)
    print(single_post.title)
    print("*******" * 5)
    print(comments)
    print(comments)
    i = 0
    for comment in comments:
        i += 1
        print(comment.comment)

    print("*******" * 5)
    print(i)

    context = {"post": single_post, "posts": posts[:4], "categories": categories[:6], "nombre_comment": i,
               "categories_post": categories_post, "comments": comments}
    return render(request, "blog/single.html", context)


def image_view(request):
    return render(request, "blog/article_01.html")


def post_view(request, slug):
    post = BlogPost.objects.get(slug=slug)
    categories_post = post.category.all()
    posts = BlogPost.objects.all().filter(published=True).exclude(slug=post.slug)
    categories = CategoryPost.objects.all()
    comments = CommentsPost.objects.all().filter(post=post)
    print(post.slug)
    print(post.title)

    context = {"post": post, "posts": posts[:4], "categories": categories[:6], "categories_post": categories_post,
               "comments": comments}

    return render(request, "blog/post_view.html", context)


def posts_view(request):
    posts = BlogPost.objects.all().filter(published=True)
    categories = CategoryPost.objects.all()
    context = {"posts": posts, "categories": posts[:4], "r_posts": posts[5:9], "categories": categories}

    return render(request, "blog/posts_view.html", context)


def category_post_view(request, category):
    category_post = CategoryPost.objects.get(cat_slug=category)
    print(category_post.title)
    posts = BlogPost.objects.all().filter(published=True, category=category_post)
    all_posts = BlogPost.objects.all().filter(published=True)[:4]
    categories = CategoryPost.objects.all()

    context = {"posts": posts, "category_post": category_post, "categories": categories, "all_posts": all_posts}

    return render(request, "blog/category_post_view.html", context)


def about_view(request):
    return render(request, "blog/about_view.html")


def contact_view(request):
    return render(request, "blog/contact_view.html")
