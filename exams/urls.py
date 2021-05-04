from django.urls import path

from .views import ExamListView, ExamRetrieveView

urlpatterns = [
    path('',ExamListView.as_view()),
    path('<int:id>/',ExamRetrieveView.as_view())
]