from django.db import models

# Create your models here.
class Students(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=30)
    stuemail = models.CharField(max_length=30)
    stuidpass = models.CharField(max_length=30)
