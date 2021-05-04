from django.db import models

# Create your models here.

class TuitionClass(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Subject(models.Model):
    tuition_class = models.ForeignKey(TuitionClass, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.tuition_class.name + ' ' + self.name