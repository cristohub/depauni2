# app/models.py
from django.db import models
from django.contrib.auth.hashers import make_password, check_password ,  is_password_usable

class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    email = models.EmailField(max_length=80, primary_key=True)
    password = models.CharField(max_length=128)  # para almacenar hash
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT)

    def __str__(self):
        return self.email

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)


    def save(self, *args, **kwargs):
        # Si la contraseña no está cifrada, la ciframos antes de guardar
        if not is_password_usable(self.password) or not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)