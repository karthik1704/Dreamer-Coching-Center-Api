from django.db import models

from classes.models import TuitionClass
# Create your models here.

class Material(models.Model):
    tuition_class  = models.ForeignKey(TuitionClass , on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    file = models.FileField(upload_to='materials/') 
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name