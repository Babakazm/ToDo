from django.db import models

class TodoItem(models.Model):
    project_name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
    done = models.BooleanField(default=False)
    deadline = models.DateField()

    def __str__(self):
        return self.project_name
