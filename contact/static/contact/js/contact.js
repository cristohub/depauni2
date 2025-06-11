
  document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('contact-form');

    if (form) {
      form.addEventListener('submit', async function (event) {
        event.preventDefault();

        const nombre = form.querySelector('[name="first_name"]').value.trim();
        const apellido = form.querySelector('[name="last_name"]').value.trim();
        const email = form.querySelector('[name="email"]').value.trim();
        const telefono = form.querySelector('[name="phone"]').value.trim();
        const comentario = form.querySelector('[name="comment"]').value.trim();

        let errores = [];

        if (!nombre) errores.push("El nombre es obligatorio.");
        if (!apellido) errores.push("El apellido es obligatorio.");
        if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) errores.push("Correo electrónico no válido.");
        if (!telefono || !/^\d{9}$/.test(telefono)) errores.push("Número de teléfono no válido. Debe tener 9 dígitos.");
        if (!comentario) errores.push("El mensaje no puede estar vacío.");

        if (errores.length > 0) {
          Swal.fire({
            icon: 'warning',
            title: 'Lo sentimos',
            html: errores.map(error => `<p>${error}</p>`).join(''),
          });
          return;
        }

        const formData = new FormData(form);

        try {
          const response = await fetch(form.action, {
            method: 'POST',
            headers: {
              'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
            },
            body: formData,
          });

          if (response.ok) {
            Swal.fire({
              icon: 'success',
              title: '¡Mensaje enviado!',
              text: 'Gracias por contactarnos. Te responderemos pronto.',
              timer: 3000,
              showConfirmButton: false
            });
            form.reset();
          } else {
            const data = await response.json();
            Swal.fire({
              icon: 'error',
              title: 'Error al enviar',
              html: Object.values(data.errors).map(err => `<p>${err[0]}</p>`).join(''),
            });
          }
        } catch (error) {
          Swal.fire({
            icon: 'error',
            title: 'Error inesperado',
            text: 'Intenta de nuevo más tarde.',
          });
        }
      });
    }
  });

