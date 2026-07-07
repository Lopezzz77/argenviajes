/* ============================================================
   SCRIPT PRINCIPAL - Navegacion, filtros, animaciones, mapa
   ============================================================ */

// Esperar a que el DOM cargue completamente
document.addEventListener('DOMContentLoaded', function() {

    /* ============================================================
       NAVEGACION MOBILE - Toggle del menu hamburguesa
       ============================================================ */
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            // Cambiar icono hamburguesa / cerrar
            const icon = this.querySelector('i');
            if (navMenu.classList.contains('active')) {
                icon.className = 'fas fa-times';
            } else {
                icon.className = 'fas fa-bars';
            }
        });

        // Cerrar menu al hacer click en un enlace
        navMenu.querySelectorAll('.nav-link').forEach(function(link) {
            link.addEventListener('click', function() {
                navMenu.classList.remove('active');
                const icon = navToggle.querySelector('i');
                if (icon) icon.className = 'fas fa-bars';
            });
        });
    }

    /* ============================================================
       NAVBAR - Efecto de sombra al scrollear
       ============================================================ */
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    /* ============================================================
       ANIMACIONES AL HACER SCROLL - Intersection Observer
       ============================================================ */
    const animateElements = document.querySelectorAll('.animate-on-scroll');

    if (animateElements.length > 0 && 'IntersectionObserver' in window) {
        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    // Dejar de observar una vez visible
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });

        animateElements.forEach(function(el) {
            observer.observe(el);
        });
    } else {
        // Fallback para navegadores sin IntersectionObserver
        animateElements.forEach(function(el) {
            el.classList.add('visible');
        });
    }

    /* ============================================================
       FILTROS POR REGION - Mostrar/ocultar provincias
       ============================================================ */
    const filterBtns = document.querySelectorAll('.filter-btn');
    const provinceCards = document.querySelectorAll('.province-card[data-region]');

    if (filterBtns.length > 0) {
        filterBtns.forEach(function(btn) {
            btn.addEventListener('click', function() {
                // Remover active de todos
                filterBtns.forEach(function(b) { b.classList.remove('active'); });
                this.classList.add('active');

                const filter = this.getAttribute('data-filter');

                provinceCards.forEach(function(card) {
                    if (filter === 'all' || card.getAttribute('data-region') === filter) {
                        card.style.display = 'flex';
                        // Re-trigger animation
                        card.classList.remove('visible');
                        void card.offsetWidth; // Reflow
                        card.classList.add('visible');
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });
    }

    /* ============================================================
       MAPA DEL DESTINO - Leaflet.js con marcador
       ============================================================ */
    window.initDestinationMap = function() {
        const mapContainer = document.getElementById('destinationMap');
        if (!mapContainer) return;

        const lat = parseFloat(mapContainer.getAttribute('data-lat'));
        const lng = parseFloat(mapContainer.getAttribute('data-lng'));
        const name = mapContainer.getAttribute('data-name');
        const province = mapContainer.getAttribute('data-province');

        if (isNaN(lat) || isNaN(lng)) {
            mapContainer.innerHTML = '<div class="map-placeholder">' +
                '<i class="fas fa-map-marked-alt"></i>' +
                '<h3>Mapa no disponible</h3>' +
                '<p>Coordenadas no definidas para este destino.</p>' +
                '<p class="map-coords">Agregá latitud y longitud en el panel de administración.</p>' +
                '</div>';
            return;
        }

        try {
            const map = L.map('destinationMap').setView([lat, lng], 13);

            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
                maxZoom: 18
            }).addTo(map);

            // Marcador principal
            const marker = L.marker([lat, lng]).addTo(map);
            marker.bindPopup('<b>' + name + '</b><br>' + province + ', Argentina').openPopup();

            // Forzar recalculacion del mapa despues de mostrar
            setTimeout(function() { map.invalidateSize(); }, 300);
        } catch (e) {
            console.error('Error al cargar el mapa:', e);
            mapContainer.innerHTML = '<div class="map-placeholder">' +
                '<i class="fas fa-map-marked-alt"></i>' +
                '<h3>Error al cargar el mapa</h3>' +
                '<p>No se pudo inicializar el mapa. Verificá tu conexión a internet.</p>' +
                '</div>';
        }
    };

    /* ============================================================
       CALCULADORA DE PRECIO - Calcular total segun estadia
       ============================================================ */
    window.initPriceCalculator = function(pricePerNight) {
        const nightsInput = document.getElementById('nightsInput');
        const peopleInput = document.getElementById('peopleInput');
        const totalPrice = document.getElementById('totalPrice');

        if (!nightsInput || !totalPrice) return;

        function updatePrice() {
            const nights = parseInt(nightsInput.value) || 1;
            const people = parseInt(peopleInput ? peopleInput.value : 1) || 1;
            const total = pricePerNight * nights * people;
            totalPrice.textContent = '$' + total.toLocaleString('es-AR');
        }

        nightsInput.addEventListener('input', updatePrice);
        if (peopleInput) peopleInput.addEventListener('input', updatePrice);
        updatePrice();
    };

    /* ============================================================
       SELECTOR DE ESTRELLAS - Sistema de valoracion
       ============================================================ */
    window.initStarRating = function() {
        const starsInput = document.getElementById('starsInput');
        const ratingValue = document.getElementById('ratingValue');
        if (!starsInput || !ratingValue) return;

        const stars = starsInput.querySelectorAll('.fa-star');

        stars.forEach(function(star) {
            star.addEventListener('mouseenter', function() {
                const value = parseInt(this.getAttribute('data-value'));
                stars.forEach(function(s) {
                    const sv = parseInt(s.getAttribute('data-value'));
                    s.style.color = sv <= value ? '#fbbf24' : '#e5e7eb';
                });
            });

            star.addEventListener('click', function() {
                const value = parseInt(this.getAttribute('data-value'));
                ratingValue.value = value;
                stars.forEach(function(s) {
                    const sv = parseInt(s.getAttribute('data-value'));
                    s.classList.toggle('active', sv <= value);
                    s.style.color = sv <= value ? '#fbbf24' : '#e5e7eb';
                });
            });
        });

        starsInput.addEventListener('mouseleave', function() {
            const selected = parseInt(ratingValue.value);
            stars.forEach(function(s) {
                const sv = parseInt(s.getAttribute('data-value'));
                s.style.color = sv <= selected ? '#fbbf24' : '#e5e7eb';
            });
        });

        const defaultVal = parseInt(ratingValue.value);
        stars.forEach(function(s) {
            const sv = parseInt(s.getAttribute('data-value'));
            if (sv <= defaultVal) s.classList.add('active');
            s.style.color = sv <= defaultVal ? '#fbbf24' : '#e5e7eb';
        });
    };

    /* ============================================================
       DROPDOWN MOBILE - Toggle para dropdown en movil
       ============================================================ */
    const navDropdowns = document.querySelectorAll('.nav-dropdown');
    if (window.innerWidth <= 768) {
        navDropdowns.forEach(function(dd) {
            const link = dd.querySelector('.nav-link');
            if (link) {
                link.addEventListener('click', function(e) {
                    e.preventDefault();
                    dd.classList.toggle('active');
                });
            }
        });
    }

    /* ============================================================
       EFECTO PARALLAX SUAVE - Hero con parallax
       ============================================================ */
    const heroSection = document.querySelector('.hero');
    if (heroSection) {
        window.addEventListener('scroll', function() {
            const scrollY = window.scrollY;
            if (scrollY < window.innerHeight) {
                heroSection.style.backgroundPositionY = scrollY * 0.5 + 'px';
            }
        });
    }
});
