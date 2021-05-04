from django.db import models

# Create your models here.
class Exam(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=False, auto_now_add=False, )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
