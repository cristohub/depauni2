from django.db import models
from resident.models import Resident
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from dateutil.relativedelta import relativedelta
from datetime import timedelta

class Building(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200)
    total_floors = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.name or self.address}"


class Service(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Ejemplo: Agua, Luz, Internet

    def __str__(self):
        return self.name







class Department(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='departments')
    floor = models.PositiveSmallIntegerField()
    number = models.CharField(max_length=10)
    area_m2 = models.DecimalField(max_digits=6, decimal_places=2)

    CAPACITY_CHOICES = [
        (1, '1 persona'),
        (2, '2 personas'),
    ]
    capacity = models.PositiveSmallIntegerField(choices=CAPACITY_CHOICES, default=1)

    services = models.ManyToManyField(Service, blank=True, related_name='departments')

    rent_price = models.DecimalField(max_digits=8, decimal_places=2)

    num_bedrooms = models.PositiveSmallIntegerField(default=1)
    num_bathrooms = models.PositiveSmallIntegerField(default=1)
    has_kitchen = models.BooleanField(default=True)

    comment = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('building', 'floor', 'number')

    def __str__(self):
        return f"Depto {self.number}"



class DepartmentImage(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='departments/')
    is_featured = models.BooleanField(default=False)  # Foto destacada para mostrar en tarjetas

    def __str__(self):
        return f"Foto de Depto {self.department.number} {'(Destacada)' if self.is_featured else ''}"







class Lease(models.Model):

    class LeaseStatus(models.TextChoices):
        ACTIVO = 'activo', _('Activo')
        FINALIZADO = 'finalizado', _('Finalizado')
        CANCELADO = 'cancelado', _('Cancelado')
        PENDIENTE = 'pendiente', _('Pendiente')
   
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='leases')
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name='leases')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    


    estado = models.CharField(
        max_length=10,
        choices=LeaseStatus.choices,
        default=LeaseStatus.PENDIENTE,
    )

    contrato_pdf = models.FileField(upload_to='contratos/', null=True, blank=True)

    def clean(self):
        if self.fecha_inicio > self.fecha_fin:
            raise ValidationError(_("Lo sentimos, la fecha de inicio no puede ser posterior a la fecha de fin."))

        # Verifica si hay traslapes con otros arriendos del mismo departamento
        overlapping = Lease.objects.filter(
            department=self.department,
            fecha_inicio__lte=self.fecha_fin,
            fecha_fin__gte=self.fecha_inicio
        )

        # Si se está editando un arriendo ya existente, exclúyelo de la búsqueda
        if self.pk:
            overlapping = overlapping.exclude(pk=self.pk)

        if overlapping.exists():
            raise ValidationError(_("Lo sentimos, este departamento ya está arrendado durante las fechas seleccionadas."))

    def __str__(self):
        return f"{self.resident} - {self.department} - {self.department.rent_price} ({self.fecha_inicio} a {self.fecha_fin})"
    







    
class Payment(models.Model):
    class PaymentStatus(models.TextChoices):
        PENDIENTE = 'pendiente', _('Pendiente')
        PAGADO = 'pagado', _('Pagado')
        ATRASADO = 'atrasado', _('Atrasado')
        CANCELADO = 'cancelado', _('Cancelado')

    class PaymentMethod(models.TextChoices):
        TRANSFERENCIA = 'transferencia', _('Transferencia')
        TARJETA = 'tarjeta', _('Tarjeta')
        EFECTIVO = 'efectivo', _('Efectivo')
        OTRO = 'otro', _('Otro')

    lease = models.ForeignKey(Lease, on_delete=models.CASCADE, related_name='payments')
    estado = models.CharField(
        max_length=10,
        choices=PaymentStatus.choices,
        default=PaymentStatus.PENDIENTE,
    )
    metodo_pago = models.CharField(
        max_length=15,
        choices=PaymentMethod.choices,
        default=PaymentMethod.TRANSFERENCIA,
    )
    fecha_pago = models.DateField(null=True, blank=True)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField(blank=True)

    monto = models.DecimalField(max_digits=8, decimal_places=2)

    def clean(self):
        if self.fecha_desde and self.fecha_hasta and self.fecha_desde > self.fecha_hasta:
            raise ValidationError(_("Lo sentimos, la fecha de inicio no puede ser posterior a la fecha de fin."))

    def save(self, *args, **kwargs):
        self.monto = self.lease.department.rent_price
        if self.fecha_desde and not self.fecha_hasta:
            self.fecha_hasta = self.fecha_desde + relativedelta(months=1) - timedelta(days=1)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pago de {self.lease.resident} ({self.fecha_desde} a {self.fecha_hasta}) - {self.monto} €"