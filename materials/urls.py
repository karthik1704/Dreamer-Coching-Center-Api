from django.urls import path

from materials.views import MaterialListView


urlpatterns = [
    path('', MaterialListView.as_view())
]