from django.urls import path

from timetables.views import TimeTableListView


urlpatterns = [
    path('', TimeTableListView.as_view())
]