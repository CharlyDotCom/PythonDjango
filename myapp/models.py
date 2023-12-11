from django.db import models

# Create your models here.


class Project(models.Model):
    ''' Representación de un proyecto informático '''
    name = models.CharField(max_length=200)
    description = models.TextField(default='')
    def __str__(self):
        return self.name
    

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' - ' + self.project.name
