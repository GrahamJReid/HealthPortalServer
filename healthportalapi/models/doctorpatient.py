from django.db import models
from healthportalapi.models import User

class DoctorPatient(models.Model):
    """Model that represents a timelineEvent"""
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor')
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient')