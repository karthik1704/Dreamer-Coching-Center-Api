from classes.models import Subject
from django.contrib import admin
from django import forms

from profiles.models import Profile
# Register your models here.

class ProfileForm(forms.ModelForm):
    class  Meta:
        model = Profile
        fields = '__all__'
    def __init__(self,instance, *args, **kwargs):
        super(ProfileForm, self).__init__( instance,*args, **kwargs)
        self.fields['subject'].queryset = Subject.objects.none()
        if instance.tuition_class:
           self.fields['subject'].queryset = Subject.objects.filter(tuition_class= instance.tuition_class) 

class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'student_name', 'tuition_class', 'phone_number')
    form = ProfileForm

    class Media:
        js = ('profiles/app.js',)

    def student_name(self, obj):
        return obj.user.first_name + ' ' + obj.user.last_name

   


admin.site.register(Profile, ProfileAdmin)
