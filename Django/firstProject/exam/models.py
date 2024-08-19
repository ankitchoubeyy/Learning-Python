from django.db import models

# Create your models here.
class Announcement(models.Model):
    aNo = models.IntegerField()
    aMsg = models.CharField(max_length=60)
    
    
