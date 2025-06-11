from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import JsonResponse
from .forms import MessageForm


def contact_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            mensaje = form.save()

            subject = 'DepaUni | Nuevo mensaje recibido desde el formulario de contacto'
            message = (
                f"<p>Se ha recibido un nuevo mensaje a través del formulario de contacto de DepaUni.</p>"
                f"<p>Por favor, revisa la información del remitente y ponte en contacto con esta persona lo antes posible:</p>"
                f"<p><strong>Nombre completo:</strong> {mensaje.first_name} {mensaje.last_name}<br>"
                f"<strong>Correo electrónico:</strong> {mensaje.email}<br>"
                f"<strong>Teléfono:</strong> {mensaje.phone}</p>"
                f"<p><strong>Mensaje:</strong><br>{mensaje.comment}</p>"
                f"<hr>"
                f"<p><em>Este mensaje ha sido enviado automáticamente. No respondas a este correo.<br>"
                f"Para contactar al remitente, utiliza directamente su correo electrónico o número de teléfono.</em></p>"
            )

            email = EmailMessage(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                ['cristofersani04@gmail.com'],
            )
            email.content_subtype = 'html'

            try:
                email.send()

                # Si la petición es AJAX, respondemos JSON
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'success': True})

                # Si no, usar mensajes y redirigir normalmente
                messages.success(request, 'Tu mensaje ha sido enviado correctamente.')
                return redirect('contact')

            except Exception as e:
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'success': False, 'error': str(e)})

                messages.error(request, f'Lo sentimos, ocurrió un error al enviar el correo: {e}')

        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors})

            messages.error(request, 'Lo sentimos, hay errores en el formulario. Revisa los campos e inténtalo de nuevo.')

    else:
        form = MessageForm()

    return render(request, 'contact/contact_form.html', {'form': form})
