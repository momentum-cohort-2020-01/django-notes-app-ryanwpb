from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=140)
    body =  models.TextField(max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Note title: {self.title} body: {self.body}"

