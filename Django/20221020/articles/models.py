from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db import models

# Create your models here.

from django.conf import settings

class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    image = ProcessedImageField(upload_to='articles/images', blank=True)
    thumbnail =  ProcessedImageField(upload_to='articles/images', blank=True,
                                processors=[ResizeToFill(240, 300)],
                                format='JPEG',
                                options={'quality': 70})
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=80)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)