from django.db import models
from .users import User

class PatientIntakeForm(models.Model):
    """Model that represents a post"""
    patient = models.ForeignKey(User, on_delete=models.CASCADE,db_column='patient_id')
    name = models.CharField(max_length=1000)
    date = models.DateField()
    email = models.CharField(max_length=1000)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=1000)
    state = models.CharField(max_length=50)
    zip = models.IntegerField()
    phonenumber = models.CharField(max_length=50)
    sex = models.CharField(max_length=1000)
    birthdate = models.DateField()
    socialsecurity = models.IntegerField()
    emergencycontactname = models.CharField(max_length=1000)
    emergencycontactphone = models.CharField(max_length=1000)
    
