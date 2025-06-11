
from django.shortcuts import render, redirect, get_object_or_404
from .models import Resident 
from authentication.models import Usuario 
from authentication.decorators import role_required
from django.views.decorators.cache import never_cache
from rent.models import Payment , Lease


@role_required('Residente')
@never_cache
def dashboard(request):
    user_name = request.session.get('user_name', 'Residente')
    return render(request, 'resident/dashboard.html', {'user_name': user_name})






@role_required('Residente')
@never_cache
def profile_view(request):
    try:
        usuario = Usuario.objects.get(email=request.session['usuario_email'])
        resident = Resident.objects.get(user=usuario)
    except (Usuario.DoesNotExist, Resident.DoesNotExist):
        resident = None

    return render(request, 'resident/profile.html', {'resident': resident})




@never_cache
def payment_view(request):
    try:
        usuario = Usuario.objects.get(email=request.session['usuario_email'])
        resident = Resident.objects.get(user=usuario)
    except (Usuario.DoesNotExist, Resident.DoesNotExist):
        resident = None

    payments = Payment.objects.filter(lease__resident=resident).order_by('-fecha_desde') if resident else []

    return render(request, 'resident/payment.html', {'resident': resident, 'payments': payments,
    })


@role_required('Residente')
@never_cache
def lease_view(request):
    user_name = request.session.get('user_name', 'Residente')

    try:
        usuario = Usuario.objects.get(email=request.session['usuario_email'])
        resident = Resident.objects.get(user=usuario)
    except (Usuario.DoesNotExist, Resident.DoesNotExist):
        resident = None

    if resident:
        leases = Lease.objects.filter(resident=resident, estado=Lease.LeaseStatus.ACTIVO)
    else:
        leases = []

    return render(request, 'resident/leases.html', {
        'uresident': resident,
        'leases': leases,
    })