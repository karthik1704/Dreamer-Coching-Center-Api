from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from classes.models import TuitionClass
from classes.serializers import TuitionClassSerializer
# Create your views here.

class TuitionClassListView(ListAPIView):

    queryset = TuitionClass.objects.all()
    serializer_class = TuitionClassSerializer
    permission_classes = [IsAuthenticated]