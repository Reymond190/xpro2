from django.db import models

# Create your models here.
class timedtest(models.Model):
    name = models.CharField(null=False)
    password = models.CharField(null=False)
    total_time = models.DateTimeField(auto_now_add=True,blank=True)
    interrupt = models.BooleanField(default=False)
    cheat_check = models.CharField(blank=True,default='not_cheated_yet')
