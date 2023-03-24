from django.http import HttpResponse


def index(request):
    return HttpResponse("Страница приложения.")

def categories(request):
    return HttpResponse("Страница с категориями")
