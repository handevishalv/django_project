from django.db import models


# Create your models here.
class Members(models.Model):
    real_name = models.CharField('realname', max_length=100)
    tx = models.CharField('tx', max_length=100)
    activity_periods = models.ForeignKey('ActivityPeriods',on_delete=models.CASCADE, related_name='memberref',null=True)

class ActivityPeriods(models.Model):
    start_time =models.DateTimeField()
    end_time =models.DateTimeField()


