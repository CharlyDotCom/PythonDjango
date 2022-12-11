from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask, CreateNewProject
# Create your views here.


def Index(request):
    title = 'Django Course!!'
    return render(request, 'index.html', {
        'title': title
    })


def About(request):
    username = 'Charly'
    return render(request, 'about.html', {
        'username': username
    })


def Hello(request, username):
    print(type(username))
    print(username)
    return HttpResponse("<h1>Hello %s </h1>" % username)


def Projects(request):
    projects = Project.objects.all
    return render(request, 'projects/projects.html', {
        'projects': projects
    })


def Tasks(request):
    tasks = Task.objects.all
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })


def create_task(request):
    if request.method == 'GET':
        # show interface
        return render(request, 'tasks/create_task.html', {
        'form': CreateNewTask()
        })

    else:
        Task.objects.create(title=request.POST['title'],
                        description=request.POST['description'], project_id=1
                        )
        return redirect('/tasks/')


def create_project(request):
    if request.method == 'GET':
        # show interface
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        project = Project.objects.create(name=request.POST['name'])
        return redirect('/projects/')     
    