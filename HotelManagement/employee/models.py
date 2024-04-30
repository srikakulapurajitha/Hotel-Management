from django.db import models

#create empdetails.
class GenderField(models.CharField):
    description = "A field to represent gender"


GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)

class employeedetails(models.Model):
    EMPLOYEE_ID=models.AutoField(primary_key=True)
    EMPLOYEE_NAME=models.CharField(max_length=30)
    DATE_OF_JOINING=models.CharField(max_length=30)
    SALARY=models.BigIntegerField()
    MOBILE=models.CharField(max_length=10)
    DESIGNATION=models.CharField(max_length=30)
    GENDER = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)