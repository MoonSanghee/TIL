from django.db import models

# Create your models here.
class todos(models.Model):
    # 첫글자 대문자로 작성해 줄 것
    content = models.CharField(max_length=80)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=3)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)