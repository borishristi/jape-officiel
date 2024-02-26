from django.http import HttpResponse


def base_view(request):
    return HttpResponse("<h1>Ok c'est bon!!!</h1>")