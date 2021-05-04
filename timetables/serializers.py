from rest_framework import serializers

from timetables.models import TimeTable, Period

class PeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Period
        fields = '__all__'


class TimeTableSerializer(serializers.ModelSerializer):
    period = PeriodSerializer(many=True, read_only=True)
    class Meta:
        model = TimeTable
        fields = '__all__'