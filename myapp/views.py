from django.http import HttpResponse
# Create your views here.


def Hello(request):
    return HttpResponse("<h1>Hello World</h1>")

def About(request):
    return HttpResponse("<h3>About</h3>")