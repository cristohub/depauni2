from django.db import models
from authentication.models import Usuario

class Tecnico(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    photo = models.ImageField(upload_to='tecnicos/', blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name1 = models.CharField(max_length=100)
    last_name2 = models.CharField(max_length=100, blank=True, null=True)
    identity_document = models.CharField(max_length=20, unique=True)

    OFICIO_CHOICES = [
        ('INF', 'Informática'),
        ('PLO', 'Plomería'),
        ('ELE', 'Electricidad'),
    ]
    oficio = models.CharField(max_length=3, choices=OFICIO_CHOICES)

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    phone = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        if self.last_name2:
            return f"{self.first_name} {self.last_name1} {self.last_name2}"
        return f"{self.first_name} {self.last_name1}"