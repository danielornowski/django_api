from django.db import models


PROJECT_STATUS = (
    ('Nowy', 'Nowy'),
    ('Zakończony', 'Zakończony')
)


class Project(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField(blank=True, default=None, null=True)
    status = models.CharField(choices=PROJECT_STATUS, max_length=30, default='Nowy')

    def __str__(self):
        return str(self.name)


class Comment(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    add_date = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=255)
