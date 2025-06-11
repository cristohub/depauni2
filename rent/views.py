from django.shortcuts import render, get_object_or_404
from .models import Department, DepartmentImage
from datetime import date

def departamentos_disponibles(request):
    hoy = date.today()
    departamentos = Department.objects.exclude(
        leases__fecha_inicio__lte=hoy,
        leases__fecha_fin__gte=hoy
    ).prefetch_related('images', 'services', 'building')

    # Agregamos la imagen destacada a cada departamento como un atributo
    for depto in departamentos:
        imagen_destacada = depto.images.filter(is_featured=True).first()
        if not imagen_destacada:
            imagen_destacada = depto.images.first()  # cualquier imagen si no hay destacada
        depto.imagen_destacada_url = imagen_destacada.image.url if imagen_destacada else None

    return render(request, 'rent/lista.html', {
        'departamentos': departamentos
    })





def detalle_departamento(request, id):
    depto = get_object_or_404(Department.objects.prefetch_related('services', 'images'), id=id)
    imagen_destacada = depto.images.filter(is_featured=True).first()
    return render(request, 'rent/detalle_depa.html', {
        'depto': depto,
        'imagen_destacada': imagen_destacada,
    })
