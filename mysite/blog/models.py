from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Voetbalspelers(models.Model):
    naam = models.CharField(max_length=100)  # Naam van de voetballer
    actuele_club = models.CharField(max_length=100)  # Actuele voetbalclub
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)  # Naam van de auteur
    datum_invoer = models.DateTimeField(default=timezone.now)  # Datum van invoer
    datum_laatste_aanpassing = models.DateTimeField(auto_now=True)  # Datum van laatste aanpassing

    def __str__(self):
        return self.naam  # Zorgt ervoor dat de naam van de voetballer wordt weergegeven in de admin-interface

    def save(self, *args, **kwargs):
        # Pas hier iets aan als je meer functionaliteit aan de save-functie wilt toevoegen
        super().save(*args, **kwargs)

# Create your models here.
