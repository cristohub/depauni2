from django.db import models

# Create your models here.

class Message(models.Model):
    first_name = models.CharField(max_length=100)  # Para el nombre
    last_name = models.CharField(max_length=100)   # Para el apellido
    email = models.EmailField()  # Para el email
    phone = models.CharField(max_length=20, blank=True, null=True)  # Para el teléfono (opcional)
    comment = models.TextField()  # Para el comentario
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'