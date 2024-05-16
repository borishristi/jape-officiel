from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

User = get_user_model()

# Create your views here.
from blog.forms import ContactUsForm
from blog.models import BlogPost, CategoryPost, CommentsPost, TagPost, ContactForm


def base_view(request):
    return render(request, "base.html")
    # return HttpResponse("<h1>Ok c'est bon!!!</h1>")


def home_view(request):
    post = BlogPost.objects.first()
    posts = BlogPost.objects.all().filter(published=True)

    categories = CategoryPost.objects.all()

    # print(posts[0].title)
    # print(posts[2].title)
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
    trending_posts = BlogPost.objects.all()[10:15]

    # randomly select 4 posts from the database, starting with post 4
    random_posts = BlogPost.objects.all().filter(published=True)[3:7]
    featured_posts = BlogPost.objects.all().filter(published=True)[7:12]

    # Popular Post
    popular_posts = BlogPost.objects.filter(published=True).order_by("-read_count")
    popular_posts_1 = BlogPost.objects.filter(published=True).order_by("-read_count")[2:4]
    popular_posts_2 = BlogPost.objects.filter(published=True).order_by("-read_count")[4:6]
    popular_post_1 = popular_posts[0]
    popular_post_2 = popular_posts[1]

    # Latest
    latest_posts = BlogPost.objects.filter(published=True)
    latest_posts_1 = latest_posts[2:4]
    latest_posts_2 = latest_posts[4:6]
    latest_post_1 = latest_posts[0]
    print(latest_post_1.title)
    latest_post_2 = latest_posts[1]
    print(latest_post_2.title)

    # Tags
    tags = TagPost.objects.all()
    print("**************************************")
    print(tags)
    # for popular in popular_posts:
    #     print("**" * 25)
    #     print(popular.title, "Read count: ", popular.read_count)

    # category post select
    categories = CategoryPost.objects.all()
    cat_1 = categories[1]
    cat_2 = categories[2]
    cat_3 = categories[3]
    cat_4 = categories[4]
    # print("***" * 15)
    # print(type(categories[3]))
    # print(categories[1])

    # posts = BlogPost.objects.all().filter(published=True, category=category_post)
    # category_post = CategoryPost.objects.get(cat_slug=category)

    category_posts_1 = BlogPost.objects.all().filter(published=True, category=cat_1)
    category_posts_2 = BlogPost.objects.all().filter(published=True, category=cat_2)
    category_posts_3 = BlogPost.objects.all().filter(published=True, category=cat_3)
    category_posts_4 = BlogPost.objects.all().filter(published=True, category=cat_4)

    i_post_1 = i_posts[0]
    i_post_2 = i_posts[1]
    i_post_3 = i_posts[2]
    context = {"post": i_post, "post_1": i_post_1, "post_2": i_post_2, "post_3": i_post_3, "posts": i_posts[4:10],
               "r_posts": i_posts[:4], "categories": categories, "random_posts": random_posts,
               "featured_posts": featured_posts, "cat_1": cat_1, "cat_2": cat_2, "cat_3": cat_3, "cat_4": cat_4,
               "categories_1": category_posts_1[:3], "categories_2": category_posts_2, "categories_3": category_posts_3,
               "categories_4": category_posts_4, "trending_posts": trending_posts, "popular_posts": popular_posts,
               "popular_post_1": popular_post_1, "popular_post_2": popular_post_2, "popular_posts_1": popular_posts_1,
               "popular_posts_2": popular_posts_2, "latest_posts_1": latest_posts_1, "latest_posts_2": latest_posts_2,
               "latest_post_1": latest_post_1, "latest_post_2": latest_post_2, "tags": tags}
    return render(request, "blog/index.html", context)


def tag_view(request, tag):
    tag_post = TagPost.objects.get(tag_slug=tag)
    # print("_"*50)
    # print(f"Le tag post est : {tag_post} et l'id est {tag_post.id} et le tag est {tag_post.tag_slug}")
    # print("_"*100)
    # for post in tag_post:
    #     print("*" * 25)
    #     print(post.title)
    posts = BlogPost.objects.all().filter(published=True, tag=tag_post)[:4]
    all_posts = BlogPost.objects.all().filter(published=True).exclude(tag=tag_post)[:5]
    other_posts = BlogPost.objects.all().filter(published=True, tag=tag_post)[4:12]
    for post in posts:
        print("*" * 25)
        print(f"Le titre du post est : {post.title}")
        print("*" * 25)

    # Pagination
    other_posts = BlogPost.objects.all().filter(published=True)[4:105]
    paginator = Paginator(other_posts, 6)
    page = request.GET.get("page")
    try:
        p_posts = paginator.page(page)
    except PageNotAnInteger:
        p_posts = paginator.page(1)
    except EmptyPage:
        p_posts = paginator.page(paginator.num_pages)

    # page_obj = paginator.get_page(page)
    print("le nombre de page est :")
    print(page)

    # Tags
    tags = TagPost.objects.all()
    categories = CategoryPost.objects.all()

    context = {"posts": posts, "category_post": tag_post, "other_posts": other_posts, "p_posts": p_posts,
               "page": page, "all_posts": all_posts, "tags": tags, "categories": categories}
    return render(request, "blog/tag.html", context)


def category2_view(request, category):
    category_post = CategoryPost.objects.get(cat_slug=category)
    posts = BlogPost.objects.all().filter(published=True, category=category_post)[:4]
    all_posts = BlogPost.objects.all().filter(published=True).exclude(category=category_post)[:5]
    other_posts = BlogPost.objects.all().filter(published=True, category=category_post)[4:12]
    # for post in posts:
    #     print("*" * 25)
    #     print(post.title)

    # Pagination
    other_posts = BlogPost.objects.all().filter(published=True)[4:105]
    paginator = Paginator(other_posts, 6)
    page = request.GET.get("page")
    try:
        p_posts = paginator.page(page)
    except PageNotAnInteger:
        p_posts = paginator.page(1)
    except EmptyPage:
        p_posts = paginator.page(paginator.num_pages)

    # page_obj = paginator.get_page(page)
    print("le nombre de page est :")
    print(page)

    # Tags
    tags = TagPost.objects.all()
    categories = CategoryPost.objects.all()

    context = {"posts": posts, "category_post": category_post, "other_posts": other_posts, "p_posts": p_posts,
               "page": page, "all_posts": all_posts, "tags": tags, "categories": categories}
    return render(request, "blog/category.html", context)


def contact2_view(request):
    # Tags and categories
    tags = TagPost.objects.all()
    categories = CategoryPost.objects.all()
    notification = ""

    # Formulaire
    if request.method == 'POST':
        # form = ContactUsForm(request.POST)
        print("_" * 50)
        print(f"La méthode d'envoie est : {request.method}")
        print("_" * 50)

        # Récupération des données
        form = ContactForm()
        form.name = request.POST.get("name")
        form.email = request.POST.get("email")
        form.subject = request.POST.get("subject")
        form.message = request.POST.get("message")
        cgu_accept = request.POST.get("cgu_accept")

        # print("*" * 100)
        # print("Affichage des données récupérées")
        # print(f"Le nom est : {form.name}")
        # print(f"L'email est : {form.email}")
        # print(f"Le sujet est : {form.subject}")
        # print(f"Le message est : {form.message}")
        # print(f"Le cgu est : {form.cgu_accept}")

        # Vérification des emails dans la base de données
        list_contacts = ContactForm.objects.all()
        my_list_contacts = []
        for contact in list_contacts:
            my_list_contacts.append(contact.email)
        if form.email in my_list_contacts:
            notification = "<span class='text-danger'>L'email est déjà dans la base de donnée</span>"
        else:
            notification = "<span class='text-success'>Enregistrement effectué avec success</span>"

            # Send mail
            subject = f"Message de {form.name}"
            body = f"""
                Name: {form.name}
                Email: {form.email}
                Subject: {form.subject}
                Message: {form.message}
            """
            send_mail(subject, body, form.email, ['japeofficiel@gmail.com'])
            form.save()
            form.clean()

    context = {"tags": tags, "categories": categories, "notification": notification}

    return render(request, "blog/contact.html", context)


def blog_view(request):
    # select the first post
    blog = BlogPost.objects.all()

    # select the all published posts
    i_posts = BlogPost.objects.all().filter(published=True)
    trending_posts = BlogPost.objects.all()[10:15]

    # randomly select 4 posts from the database, starting with post 4
    random_posts = BlogPost.objects.all().filter(published=True)[3:7]

    # Popular Post
    popular_posts = BlogPost.objects.filter(published=True).order_by("-read_count")
    popular_posts_1 = BlogPost.objects.filter(published=True).order_by("-read_count")[2:4]
    popular_posts_2 = BlogPost.objects.filter(published=True).order_by("-read_count")[4:6]
    popular_post_1 = popular_posts[0]
    popular_post_2 = popular_posts[1]

    # Latest
    latest_posts = BlogPost.objects.filter(published=True)
    latest_posts_1 = latest_posts[2:4]
    latest_posts_2 = latest_posts[4:6]
    latest_post_1 = latest_posts[0]
    print(latest_post_1.title)
    latest_post_2 = latest_posts[1]
    print(latest_post_2.title)

    # Tags
    tags = TagPost.objects.all()
    print("**************************************")
    print(tags)

    # category post select
    categories = CategoryPost.objects.all()
    cat_1 = categories[1]

    i_post_1 = i_posts[0]
    i_post_2 = i_posts[1]
    i_post_3 = i_posts[2]
    context = {"blog": blog, "post_1": i_post_1, "post_2": i_post_2, "post_3": i_post_3, "posts": i_posts[4:10],
               "r_posts": i_posts[:4], "categories": categories, "random_posts": random_posts,
               "cat_1": cat_1, "trending_posts": trending_posts,
               "popular_posts": popular_posts,
               "popular_post_1": popular_post_1, "popular_post_2": popular_post_2, "popular_posts_1": popular_posts_1,
               "popular_posts_2": popular_posts_2, "latest_posts_1": latest_posts_1, "latest_posts_2": latest_posts_2,
               "latest_post_1": latest_post_1, "latest_post_2": latest_post_2, "tags": tags}
    return render(request, "blog/blog.html", context)


def single_view(request, slug):
    single_post = BlogPost.objects.get(slug=slug)
    categories_post = single_post.category.all()
    posts = BlogPost.objects.all().filter(published=True).exclude(slug=single_post.slug)
    categories = CategoryPost.objects.all()
    comments = CommentsPost.objects.all().filter(post=single_post.id)

    # Enregistrement d'un commentaire'
    if request.method == "POST":
        comment = CommentsPost()
        comment.post = single_post
        comment.author = request.user
        print(f"l'utilisateur est : {request.user.id}")

        comment.comment = request.POST.get("message")
        print("*"*50)
        print(f"Impression du commentaire: {request.POST.get('message')}")
        print(comment.comment)
        print(comment.author)
        print(comment.post)

        comment.save()

    single_post.read_count += 1
    single_post.save()

    # Tags and categories
    tags = TagPost.objects.all()
    post_tags = single_post.tag.all()
    for post_tag in post_tags:
        print(post_tag.title)

    i = 0
    for comment in comments:
        i += 1

    print("*******" * 5)
    print(i)

    context = {"post": single_post, "posts": posts[:4], "categories": categories[:6], "nombre_comment": i,
               "categories_post": categories_post, "comments": comments, "tags": tags, "post_tags": post_tags}
    return render(request, "blog/single.html", context)


def save_comment(request):
    # Enregistrement d'un commentaire'
    print("Test de save_contact")
    if request.method == "POST":
        comment = CommentsPost()
        comment.comment = request.POST.get("comment")
        print(comment.comment)
        # comment.comment = request.POST.get("post")
        # comment.comment = request.POST.get("comment")
        # comment.comment = request.POST.get("comment")


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
