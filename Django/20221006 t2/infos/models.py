from django.db import models

# Create your models here.
class Infos(models.Model):
    title = models.CharField(max_length=30)
    director = models.CharField(max_length=30)
    summary = models.TextField()
    opening_date = models.DateField()
    running_time = models.IntegerField()