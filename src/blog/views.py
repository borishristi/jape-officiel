from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def base_view(request):
    return render(request, "base.html")
    # return HttpResponse("<h1>Ok c'est bon!!!</h1>")


def image_view(request):
    return render(request, "blog/article_01.html")