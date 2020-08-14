from django.shortcuts import render
from rest_framework import viewsets
from .models import ActivityPeriods,Members
from .serializers import ActivityPeriodsSerializer,MembersSerializer
# Create your views here.
class MemberView(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer

class ActivityPeriodsView(viewsets.ModelViewSet):
    queryset = ActivityPeriods.objects.all()
    serializer_class = ActivityPeriodsSerializer