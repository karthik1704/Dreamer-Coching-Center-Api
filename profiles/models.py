from django.db import models
from django.conf import settings
from django.db.models.deletion import DO_NOTHING

from classes.models import Subject, TuitionClass
# Create your models here.

USER = settings.AUTH_USER_MODEL

gender = (
    ('Male','Male'),
    ('Female','Female'),
)

class Profile(models.Model):
    user = models.OneToOneField(USER, on_delete=models.CASCADE, limit_choices_to={'is_student':True})
    tuition_class = models.ForeignKey(TuitionClass, on_delete=models.DO_NOTHING)
    subject = models.ManyToManyField(Subject)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    mother_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(choices=gender, max_length=20)
    dob = models.DateField(verbose_name='Date of Birth')
    address = models.TextField()
    phone_number = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='students', blank=True, null=True)

    def __str__(self):
        return self.user.first_name + self.user.last_name