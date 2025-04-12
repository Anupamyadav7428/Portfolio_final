from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=200)
    message =models.TextField(max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    