from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from timetables.models import TimeTable
from timetables.serializers import TimeTableSerializer
# Create your views here.

class TimeTableListView(ListAPIView):
    queryset = TimeTable.objects.none()
    serializer_class = TimeTableSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        queryset = TimeTable.objects.filter(tuition_class = self.request.user.profile.tuition_class)
        return queryset