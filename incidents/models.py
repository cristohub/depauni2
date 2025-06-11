from django.db import models
from rent.models import Department
from tecnico.models import Tecnico 
# Create your models here.


class Averia(models.Model):
    


    TIPO_AVERIA = [
        ('electrica', 'Eléctrica'),
        ('agua', 'Agua'),
        ('wifi', 'Wi-Fi'),
        ('otro', 'Otro'),
    ]




    

    departamento = models.ForeignKey(Department, on_delete=models.CASCADE)
    descripcion = models.TextField()
    tipo_averia = models.CharField(max_length=20, choices=TIPO_AVERIA)
    fecha_reporte = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='pendiente')
    coste = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Avería en {self.departamento} - {self.tipo_averia}"
    



class AveriaTecnico(models.Model):
    averia = models.OneToOneField(Averia, on_delete=models.CASCADE)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_resuelta = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Actualizar estado en Averia según fecha_resuelta
        if self.fecha_resuelta:
            self.averia.estado = 'resuelta'
        else:
            self.averia.estado = 'pendiente'  # o algún estado por defecto
        self.averia.save()

    def __str__(self):
        if self.fecha_resuelta:
            fecha = self.fecha_resuelta.strftime('%d/%m/%Y')
        else:
            fecha = "sin resolver"
        return f"Reparada por {self.tecnico} el {fecha}"