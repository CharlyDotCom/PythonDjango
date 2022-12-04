from django.http import HttpResponse
# Create your views here.

def Index(request):
    return HttpResponse("<h1>Index Page</h1>")

def Hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s </h1>" % username)

def About(request):
    return HttpResponse("<h3>About</h3>")