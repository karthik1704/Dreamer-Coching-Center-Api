from django.urls import path

from classes.views import TuitionClassListView


urlpatterns = [
    path('', TuitionClassListView.as_view()),
]