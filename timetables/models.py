from django.db import models

from classes.models import Subject, TuitionClass  
# Create your models here.

WEEK_DAYS = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
) 

PERIOD_NUMBER = (
    (1,1),
    (2,2),
    (3,3),
)

PERIOD_NAME = (
    ('Study','Study'),
    ('Test','Test'),
    ('SPL','SPL'),
)


class TimeTable(models.Model):
    tuition_class = models.ForeignKey(TuitionClass, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    day = models.CharField(choices=WEEK_DAYS, max_length=50)

    def __str__(self) -> str:
        return self.day

    def period(self):
        if not hasattr(self, '_period'):
            self._period = self.period_set.all()
            return self._period



class Period(models.Model):
    timetable = models.ForeignKey(TimeTable, on_delete=models.CASCADE)
    number = models.IntegerField(choices=PERIOD_NUMBER, default=1)
    name = models.CharField(choices=PERIOD_NAME, max_length=50)

    def __str__(self) -> str:
        return str(self.number) + ' '  + self.name
    

