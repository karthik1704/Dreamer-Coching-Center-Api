from django.contrib import admin

from timetables.models import TimeTable,Period
# Register your models here.

class PeriodInline(admin.TabularInline):
    model = Period

class TimeTableAdmin(admin.ModelAdmin):
    list_display = ('day', 'tuition_class', 'subject',  )
    inlines = (PeriodInline,)

  
        

admin.site.register(TimeTable, TimeTableAdmin)