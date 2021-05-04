from rest_framework import serializers

from classes.models import TuitionClass

class TuitionClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = TuitionClass
        fields = '__all__' 