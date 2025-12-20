from django.db import models
from .users import User

class PatientAllergyForm(models.Model):
    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="allergy_forms"
    )


    pollen = models.BooleanField(default=False)
    pet = models.BooleanField(default=False)
    mold = models.BooleanField(default=False)
    milk = models.BooleanField(default=False)
    eggs = models.BooleanField(default=False)
    nuts = models.BooleanField(default=False)
    shellfish = models.BooleanField(default=False)
    insect = models.BooleanField(default=False)
    medications = models.BooleanField(default=False)
    latex = models.BooleanField(default=False)
    other = models.TextField(blank=True)
