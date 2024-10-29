from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    link = models.URLField()
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.title

class Experience(models.Model):
    job_title = models.CharField(max_length=500)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company}"