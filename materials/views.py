from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from materials.models import Material
from profiles.models import Profile
from materials.serializers import MaterialSerializer
# Create your views here.

class MaterialListView(ListAPIView):
    queryset = Material.objects.none()
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        tclass = Profile.objects.get(user = self.request.user).tuition_class
        queryset = Material.objects.filter(tuition_class = tclass)
        return queryset