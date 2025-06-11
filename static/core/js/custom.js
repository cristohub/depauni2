let lastScrollTop = 0;
const header = document.getElementById("main-header");
const main = document.querySelector("main");

window.addEventListener("scroll", () => {
  const currentScroll = window.pageYOffset || document.documentElement.scrollTop;
  const mainTop = main.offsetTop;

  // Solo aplicar el efecto si el usuario ya ha pasado el <main>
  if (currentScroll > mainTop) {
    if (currentScroll > lastScrollTop) {
      // Scroll hacia abajo: ocultar header
      header.classList.add("header-hidden");
    } else {
      // Scroll hacia arriba: mostrar header
      header.classList.remove("header-hidden");
    }
  } else {
    // Si está arriba del main, aseguramos que el header esté visible
    header.classList.remove("header-hidden");
  }

  lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
});




document.addEventListener("DOMContentLoaded", function () {
  const elements = document.querySelectorAll(".fade-in-up, .fade-in-left, .fade-in-right");

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  elements.forEach(el => observer.observe(el));
});


document.addEventListener("DOMContentLoaded", function () {
  const counter = document.getElementById('student-counter');
  const section = document.getElementById('student-section');
  let started = false;

  if (counter && section) {
    const startCounting = () => {
      let count = 0;
      const target = 100;
      const speed = 15;

      const update = () => {
        if (count < target) {
          count++;
          counter.textContent = '+' + count;
          setTimeout(update, speed);
        } else {
          counter.textContent = '+' + target;
        }
      };

      update();
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !started) {
          started = true;
          startCounting();
        }
      });
    }, { threshold: 0.5 });

    observer.observe(section);
  }
});



document.addEventListener("DOMContentLoaded", () => {
  const frases = [
    "Vive Cerca, Aprende Mejor",
    "Tu segundo hogar junto a la uni",
    "Comodidad, estudio y tranquilidad"
  ];

  let i = 0;
  let j = 0;
  const fraseEl = document.getElementById("frase");

  function escribir() {
    if (j < frases[i].length) {
      fraseEl.textContent += frases[i][j];
      j++;
      setTimeout(escribir, 80);
    } else {
      setTimeout(() => {
        fraseEl.textContent = "";
        j = 0;
        i = (i + 1) % frases.length;
        escribir();
      }, 2000);
    }
  }

  escribir();
});


