from django.urls import path

from .views import ProfileView, get_subjects


urlpatterns = [
    path('', ProfileView.as_view()),
    path('get-subjects/', get_subjects, name='get-subjects')
]