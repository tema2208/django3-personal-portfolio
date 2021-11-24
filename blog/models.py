from django.db import models


class ProjectBlog(models.Model):
    title = models.CharField(max_length = 100)
    data_time = models.DateTimeField(max_length = 150)
    description = models.CharField(max_length = 250)
    url = models.URLField(blank = True)

    def __str__(self):
        return self.title
# Create your models here.
