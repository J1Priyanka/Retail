from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Django First Application is running on Azure.")
