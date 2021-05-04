from django.contrib import admin

from attendances.models import Attendance, StudentAttendance
from classes.models import Subject
from django.contrib.auth import get_user_model

# Register your models here.

USER = get_user_model()

class StudentAttendanceInline(admin.TabularInline):
    model=StudentAttendance
    # def formfield_for_foreignkey(self, db_field, request, **kwargs ): 
    #     if db_field.name == 'user':
    #         kwargs['queryset'] = USER.objects.filter( profile__tuition_class = request.tuition_class)
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    

class AttendanceAdmin(admin.ModelAdmin):

    list_display = ('date','tuition_class', 'total_present', 'total_absent')
    inlines = (StudentAttendanceInline,)
  
   
admin.site.register(Attendance, AttendanceAdmin)