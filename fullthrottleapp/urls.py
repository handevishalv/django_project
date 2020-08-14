from django.urls import path, include
from .views import MemberView, ActivityPeriodsView
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('member', MemberView)
routers.register('activity', ActivityPeriodsView)

urlpatterns = [
    path('', include(routers.urls)),
    ]
