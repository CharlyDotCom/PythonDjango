from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404    
# Create your views here.

def Index(request):
    return HttpResponse("<h1>Index Page</h1>")

def Hello(request, username):
    print(type(username))
    print(username)
    return HttpResponse("<h1>Hello %s </h1>" % username)

def About(request):
    return HttpResponse("<h3>About</h3>")

def Projects(request):
    prjs = list(Project.objects.values())
    return JsonResponse(prjs, safe=False);

def Tasks(request, id):
    # tas = Task.objects.get(id=id)
    tas = get_object_or_404(Task, id=id)
    return HttpResponse("<h3>Tasks: %s </h3>" % tas.title);
