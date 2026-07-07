# Sistema de Guía Turística - Argentina Viajes
- Materia: P.D.I.S.C
- Curso: 7°1
- Docente: Gareis Pablo

## Lenguajes de Programación
- Python + Django
- HTML5
- CSS3
- JavaScript

## Temática
Guía turística interactiva de provincias y destinos de Argentina, con catálogo de hoteles, reseñas de usuarios y geolocalización por trilateración.

## Integrantes
- Camila Soliz: Backend y Líder
- César López: Encargado del Frontend
- Sofía Balcazar: Documentación, marketing

---

## Cómo usar la página

### Inicio
La página principal muestra un buscador, filtros por región (Norte, Cuyo, Patagonia, etc.) y una grilla de provincias. Cada provincia lleva a sus destinos turísticos.

### Registro e inicio de sesión
Para dejar reseñas, entrar al panel de administración o usar la calculadora de geolocalización, hay que registrarse en `/registro/` e iniciar sesión en `/login/`.

### Destinos
Cada destino tiene descripción, galería de imágenes, mapa interactivo, cómo llegar (micro, avión, tren, auto), calculadora de estadía y hoteles recomendados.

### Reseñas
Los usuarios logueados pueden dejar reseñas con puntuación de 1 a 5 estrellas y comentarios. Pueden editar o eliminar sus propias reseñas.

### Panel de Administración
El usuario **admin** (usuario: `admin`, contraseña: `admin123`) puede acceder a `/panel/` para modificar provincias y destinos: precios, descripciones, imágenes (desde las disponibles en la carpeta `static/app/images/`), coordenadas, etc.

### Imágenes
Todas las imágenes de provincias y destinos se cargan desde la carpeta `app/static/app/images/`. Si una provincia o destino no tiene imagen asignada, se muestra `salta.png` por defecto.

### Geolocalización
En `/geolocalizacion/` hay una calculadora de trilateración que estima una posición a partir de distancias a tres antenas de referencia.

### Carga de datos de ejemplo
Correr `python manage.py cargar_datos` para poblar la base de datos con 10 provincias, 11 destinos, 20 hoteles, reseñas de ejemplo y dos usuarios (`admin` / `admin123` y `viajero` / `viajero123`).

### Usuarios predefinidos
| Usuario | Contraseña | Rol |
|---------|-----------|-----|
| admin   | admin123  | Superusuario (accede al panel `/panel/`) |
| viajero | viajero123 | Usuario común (puede dejar reseñas) |
