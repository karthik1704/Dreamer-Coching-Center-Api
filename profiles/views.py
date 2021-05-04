from django.db.models import query
from django.http.response import JsonResponse
from rest_framework.generics import RetrieveUpdateAPIView, get_object_or_404
from rest_framework.permissions import BasePermission, IsAuthenticated

from django.contrib.auth.decorators import login_required

from profiles.models import Profile
from profiles.serializers import ProfileSerializer

from classes.models import Subject, TuitionClass
# Create your views here.
class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class ProfileView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    # lookup_field = 'user'

    def get_object(self):
        print(self.request.user)
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user = self.request.user)
        return obj

    def perform_update(self, serializer):
        
        return super().perform_update(serializer)

    # def get_queryset(self):
    #     print(self.request.user)
    #     return Profile.objects.get(user = self.request.user)


# Admin Site Controls  views

@login_required
def get_subjects(request):
    tuition_class = request.POST.get('tuition_class')
    print(tuition_class)
    subject = {}

    
    if tuition_class:
        subjects = Subject.objects.filter(tuition_class=int(tuition_class))
        subject = {s.name:s.id for s in subjects}
   

    return JsonResponse(data=subject,safe=False)