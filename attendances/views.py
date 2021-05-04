from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import BasePermission, IsAuthenticated

from .models import Attendance
from .serializers import AttendanceSerializer

# Create your views here.
class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class AttendanceView(ListAPIView):
    queryset = Attendance.objects.none()
    serializer_class = AttendanceSerializer
    permission_classes = [IsOwner, IsAuthenticated]

