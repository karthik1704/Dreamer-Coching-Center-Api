from django.db import models
from accounts.models import User


from classes.models import TuitionClass

# Create your models here.
class Attendance(models.Model):
    tuition_class = models.ForeignKey(TuitionClass, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=255, null=True, blank=True)
    present = models.IntegerField(default=0)
    absent =  models.IntegerField(default=0)

    def __str__(self):
        return str(self.date)

    @property
    def total_present(self):
        count =  self.studentattendance_set.filter(present = True).count()
        return count
    
    @property
    def total_absent(self):
        count =  self.studentattendance_set.filter(present = False).count()
        return count
    

class StudentAttendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    present = models.BooleanField(default=False)
    in_time = models.TimeField(auto_now=True, editable=True)
    out_time = models.TimeField(null=True, blank=True)

    