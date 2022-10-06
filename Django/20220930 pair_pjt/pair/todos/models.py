from email.policy import default
from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now =True)




