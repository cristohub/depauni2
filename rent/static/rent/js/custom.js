let paginaCargada = false;

// Iniciar animación en loop
const animacion = lottie.loadAnimation({
  container: document.getElementById('animacion'),
  renderer: 'svg',
  loop: true,
  autoplay: true,
  path: '/static/rent/animaciones/AnimationLoading.json'
});

// Cuando la página esté lista, esperar a que termine la vuelta actual
window.onload = () => {
  paginaCargada = true;

  // Pausar loop al terminar la vuelta actual
  animacion.loop = false;
};

// Cuando termine la vuelta actual (tras quitar el loop)
animacion.addEventListener('complete', () => {
  if (paginaCargada) {
    document.getElementById('loading').style.display = 'none';
    document.getElementById('contenido').style.display = 'block';
  }
});
