from django.contrib import admin
from .models import Building, Service, Department, DepartmentImage, Lease, Payment

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'total_floors')
    search_fields = ('name', 'address')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class DepartmentImageInline(admin.TabularInline):
    model = DepartmentImage
    extra = 1  # Cuántas filas extra para añadir
    fields = ('image', 'is_featured')
    readonly_fields = ()
    # Puedes agregar validación para que solo haya 1 foto destacada, pero es opcional

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'number', 'building', 'floor', 'area_m2', 'capacity', 'rent_price',
        'num_bedrooms', 'num_bathrooms', 'has_kitchen'
    )
    list_filter = ('building', 'floor', 'capacity', 'has_kitchen')
    search_fields = ('number', 'building__name', 'building__address')
    filter_horizontal = ('services',)

    inlines = [DepartmentImageInline]


@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):
    list_display = ('resident', 'department', 'fecha_inicio', 'fecha_fin')
    list_filter = ('fecha_inicio', 'fecha_fin', 'department__building')
    search_fields = ('resident__first_name', 'resident__last_name', 'department__number', 'department__building__name')




@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'lease', 'estado', 'metodo_pago', 'fecha_pago', 'fecha_desde', 'fecha_hasta', 'monto')
    list_filter = ('estado', 'metodo_pago', 'fecha_pago')
    search_fields = ('lease__resident__name',)
    ordering = ('-fecha_pago',)