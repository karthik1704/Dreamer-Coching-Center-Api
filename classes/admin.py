from django.contrib import admin

from .models import TuitionClass, Subject
# Register your models here.

class SubjectInline(admin.StackedInline):
    model = Subject
    

class TuitionClassAdmin(admin.ModelAdmin):
    inlines = (SubjectInline, )

admin.site.register(TuitionClass, TuitionClassAdmin)