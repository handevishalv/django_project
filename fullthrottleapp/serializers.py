from rest_framework import serializers
from .models import Members,ActivityPeriods

class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ('id', 'real_name','tx','activity_periods')

class ActivityPeriodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriods
        fields =('start_time','end_time')
