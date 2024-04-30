from django.db import models

# creating table for booking purpose
class booking(models.Model):
    a_room=models.IntegerField()
    name=models.CharField(max_length=80)
    mobile_no=models.BigIntegerField()
    email=models.CharField(max_length=100)
    checkin=models.DateField()
    checkout=models.DateField()

