from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.models import Province, Destination, Hotel, Review

class Command(BaseCommand):
    help = "Carga datos de ejemplo: provincias, destinos y hoteles argentinos"

    def handle(self, *args, **options):
        self.stdout.write("Cargando datos de prueba...")

        # Crear superusuario si no existe
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write("  Superusuario creado: admin / admin123")

        # Usuario de prueba
        if not User.objects.filter(username='viajero').exists():
            User.objects.create_user('viajero', 'viajero@example.com', 'viajero123')
            self.stdout.write("  Usuario creado: viajero / viajero123")

        # --- PROVINCIAS ---
        provincias_data = [
            {"name": "Buenos Aires", "capital": "La Plata", "region": "bsas", "slug": "buenos-aires",
             "description": "La provincia más grande y poblada del país, con la vibrante ciudad de Buenos Aires, playas atlánticas y el delta del Paraná.",
             "image": ""},
            {"name": "Salta", "capital": "Salta", "region": "norte", "slug": "salta",
             "description": "Tierra de cerros multicolores, valles calchaquíes y la mejor arquitectura colonial del norte argentino.",
             "image": "salta.png"},
            {"name": "Mendoza", "capital": "Mendoza", "region": "cuyo", "slug": "mendoza",
             "description": "Capital del vino argentino, con el Cerro Aconcagua como telón de fondo y paisajes de montaña únicos.",
             "image": ""},
            {"name": "Bariloche", "capital": "San Carlos de Bariloche", "region": "patagonia", "slug": "rio-negro",
             "description": "La capital de los lagos patagónicos, famosa por su chocolate, nieve y paisajes de ensueño.",
             "image": "bariloche.png"},
            {"name": "Córdoba", "capital": "Córdoba", "region": "centro", "slug": "cordoba",
             "description": "Corazón geográfico del país, con sierras, ríos y una rica historia universitaria y colonial.",
             "image": ""},
            {"name": "Misiones", "capital": "Posadas", "region": "litoral", "slug": "misiones",
             "description": "Selva subtropical, las majestuosas Cataratas del Iguazú y las ruinas jesuíticas de San Ignacio.",
             "image": ""},
            {"name": "Jujuy", "capital": "San Salvador de Jujuy", "region": "norte", "slug": "jujuy",
             "description": "El Cerro de los Siete Colores, la Quebrada de Humahuaca y la cultura andina más pura del país.",
             "image": ""},
            {"name": "Neuquén", "capital": "Neuquén", "region": "patagonia", "slug": "neuquen",
             "description": "Lagunas, bosques petrificados y la cuenca del Comahue, con San Martín de los Andes como joya.",
             "image": ""},
            {"name": "Santa Fe", "capital": "Santa Fe", "region": "litoral", "slug": "santa-fe",
             "description": "La costa del río Paraná, la ciudad de Rosario y una rica tradición agropecuaria.",
             "image": ""},
            {"name": "Tierra del Fuego", "capital": "Ushuaia", "region": "patagonia", "slug": "tierra-del-fuego",
             "description": "El fin del mundo: Ushuaia, el Canal Beagle, pingüinos y paisajes australes únicos.",
             "image": ""},
        ]

        provincias = {}
        for pd in provincias_data:
            p, created = Province.objects.update_or_create(
                slug=pd["slug"],
                defaults=pd
            )
            provincias[p.slug] = p
            if created:
                self.stdout.write(f"  Provincia creada: {p.name}")

        # --- DESTINOS ---
        destinos_data = [
            # Buenos Aires
            {"province": "buenos-aires", "name": "CABA - Buenos Aires", "slug": "caba",
             "short_description": "La ciudad que nunca duerme: cultura, gastronomía, teatro y el histórico Obelisco.",
             "description": "Buenos Aires es una ciudad vibrante y cosmopolita, conocida como la París de Sudamérica. Ofrece una combinación única de arquitectura europea, tango apasionado, una escena gastronómica de primer nivel y barrios con personalidad propia como La Boca, Palermo, San Telmo y Recoleta.",
             "price_per_night": 85, "is_featured": True,
             "location_lat": -34.6037, "location_lng": -58.3816,
             "image": "https://images.unsplash.com/photo-1612294037637-ec328d0e075e?w=600",
             "images": ["https://images.unsplash.com/photo-1612294037637-ec328d0e075e?w=600", "https://images.unsplash.com/photo-1589909202802-8f4aadce1849?w=600"],
             "how_to_get": {"micro": "Desde cualquier provincia llegás en 8-12 hs. Terminal de Retiro.", "avion": "Aeropuerto Internacional Ezeiza (EZE) o Aeroparque (AEP).", "tren": "Trenes a Retiro, Once y Constitución desde el AMBA."}},
            {"province": "buenos-aires", "name": "Mar del Plata", "slug": "mar-del-plata",
             "short_description": "La playa por excelencia: arena, mar, casino y la mejor movida nocturna del verano.",
             "description": "Mar del Plata es el destino balneario más famoso de Argentina. Sus extensas playas, la emblemática Bristol, el puerto con lobos marinos y una oferta gastronómica que incluye el mejor pescado fresco la convierten en la reina del verano argentino.",
             "price_per_night": 60, "is_featured": True,
             "location_lat": -38.0055, "location_lng": -57.5426,
             "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=600",
             "images": ["https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=600"],
             "how_to_get": {"micro": "Desde Retiro (Bs As) en 4-5 hs por Ruta 2.", "avion": "Vuelos directos desde Aeroparque (1h).", "auto": "Por Autovía 2, 400 km desde CABA."}},
            # Salta
            {"province": "salta", "name": "Salta Capital", "slug": "salta-capital",
             "short_description": "La Linda: arquitectura colonial, cerros y la mejor empanada del norte.",
             "description": "Salta, conocida como 'La Linda', cautiva con su arquitectura colonial bien preservada, sus iglesias barrocas, el cerro San Bernardo y su famoso tren a las nubes. Es la puerta de entrada a los valles calchaquíes y los paisajes de altura del norte argentino.",
             "price_per_night": 55, "is_featured": True,
             "location_lat": -24.7821, "location_lng": -65.4232,
             "image": "salta.png",
             "images": ["https://images.unsplash.com/photo-1591628001891-9adec694d502?w=600"],
             "how_to_get": {"micro": "Desde Retiro en 18 hs. Terminal de Salta.", "avion": "Aeropuerto Martín Miguel de Güemes (SLA).", "tren": "Tren a las Nubes (solo turístico)."}},
            # Mendoza
            {"province": "mendoza", "name": "Mendoza Capital - Ruta del Vino", "slug": "mendoza-capital",
             "short_description": "Tierra del Malbec: bodegas, montañas y el Cerro Aconcagua.",
             "description": "Mendoza es el corazón vitivinícola de Argentina. Recorrer sus bodegas, disfrutar de la gastronomía local, hacer trekking por el Cerro Aconcagua y perderse en los paisajes de alta montaña son experiencias imperdibles. La ciudad se destaca por sus amplias avenidas arboladas y acequias.",
             "price_per_night": 70, "is_featured": True,
             "location_lat": -32.8895, "location_lng": -68.8458,
             "image": "https://images.unsplash.com/photo-1624623278313-a930126a11c3?w=600",
             "images": ["https://images.unsplash.com/photo-1624623278313-a930126a11c3?w=600"],
             "how_to_get": {"micro": "Desde Retiro en 14 hs. Terminal de Mendoza.", "avion": "Aeropuerto El Plumerillo (MDZ).", "auto": "Ruta 7, 1050 km desde CABA."}},
            # Bariloche
            {"province": "rio-negro", "name": "San Carlos de Bariloche", "slug": "bariloche",
             "short_description": "Lagos, montañas, chocolate y la mejor nieve de Sudamérica.",
             "description": "Bariloche es el destino patagónico por excelencia. Rodeada de lagos cristalinos, montañas nevadas y bosques milenarios, ofrece actividades todo el año: esquí en el Cerro Catedral, navegación por el Nahuel Huapi, excursiones al Bolsón y una tradición chocolatera única.",
             "price_per_night": 95, "is_featured": True,
             "location_lat": -41.1335, "location_lng": -71.3103,
             "image": "bariloche.png",
             "images": ["https://images.unsplash.com/photo-1582827501715-e8e7c163a77a?w=600"],
             "how_to_get": {"micro": "Desde Retiro en 22 hs. Terminal de Bariloche.", "avion": "Aeropuerto de Bariloche (BRC).", "auto": "Ruta 237 desde Neuquén."}},
            # Córdoba
            {"province": "cordoba", "name": "Villa General Belgrano", "slug": "villa-general-belgrano",
             "short_description": "Pueblo alemán en las sierras: cerveza artesanal, ríos de montaña y relax.",
             "description": "Villa General Belgrano es un encantador pueblo de estilo alemán enclavado en las sierras de Córdoba. Famoso por su Fiesta Nacional de la Cerveza, sus ríos de aguas cristalinas, la arquitectura centroeuropea y la calidez de su gente. Ideal para escapadas de relax y gastronomía.",
             "price_per_night": 50, "is_featured": False,
             "location_lat": -31.9786, "location_lng": -64.5612,
             "image": "https://images.unsplash.com/photo-1599630640671-2c69e8c7a02e?w=600",
             "images": ["https://images.unsplash.com/photo-1599630640671-2c69e8c7a02e?w=600"],
             "how_to_get": {"micro": "Desde Cordoba capital en 1.5h.", "auto": "Ruta 5 y 14 desde Cordoba.", "tren": "Tren de las Sierras (solo tramos)"}},
            # Misiones
            {"province": "misiones", "name": "Cataratas del Iguazú", "slug": "cataratas-del-iguazu",
             "short_description": "Una de las 7 maravillas naturales del mundo: agua, selva y naturaleza pura.",
             "description": "Las Cataratas del Iguazú son un espectáculo natural sin igual. Más de 275 saltos de agua rodeados de selva subtropical, con la imponente Garganta del Diablo como protagonista. Parque Nacional, paseos en lancha y una biodiversidad única te esperan en la frontera con Brasil.",
             "price_per_night": 80, "is_featured": True,
             "location_lat": -25.6953, "location_lng": -54.4367,
             "image": "https://images.unsplash.com/photo-1593273361036-f8b44a6e40d6?w=600",
             "images": ["https://images.unsplash.com/photo-1593273361036-f8b44a6e40d6?w=600"],
             "how_to_get": {"micro": "Desde Retiro en 18 hs.", "avion": "Aeropuerto Puerto Iguazú (IGR)."}},
            # Jujuy
            {"province": "jujuy", "name": "Quebrada de Humahuaca", "slug": "quebrada-humahuaca",
             "short_description": "Cerro de los Siete Colores, Purmamarca y la cultura andina más pura.",
             "description": "La Quebrada de Humahuaca es un valle de montaña declarado Patrimonio de la Humanidad. Sus cerros multicolores, los pueblos de Purmamarca, Tilcara y Humahuaca, las ferias artesanales y la imponente cultura andina crean un paisaje único en el mundo.",
             "price_per_night": 45, "is_featured": False,
             "location_lat": -23.5281, "location_lng": -65.3482,
             "image": "https://images.unsplash.com/photo-1591628001891-9adec694d502?w=600",
             "images": ["https://images.unsplash.com/photo-1591628001891-9adec694d502?w=600"],
             "how_to_get": {"micro": "Desde Salta capital en 3h.", "auto": "Ruta 9 desde Salta.", "tren": "Tren a las Nubes (cerca)"}},
            # Neuquén - San Martín de los Andes
            {"province": "neuquen", "name": "San Martín de los Andes", "slug": "san-martin-andes",
             "short_description": "Lagos cristalinos, bosques y el mejor fly fishing de la Patagonia.",
             "description": "San Martín de los Andes es una joya patagónica a orillas del lago Lácar. Rodeada de bosques de arrayanes y montañas, ofrece navegación, pesca deportiva, rafting y trekking. El Cerro Chapelco es ideal para esquí en invierno.",
             "price_per_night": 75, "is_featured": False,
             "location_lat": -40.1559, "location_lng": -71.3545,
             "image": "https://images.unsplash.com/photo-1582827501715-e8e7c163a77a?w=600",
             "images": ["https://images.unsplash.com/photo-1582827501715-e8e7c163a77a?w=600"],
             "how_to_get": {"micro": "Desde Neuquén capital en 5h.", "avion": "Aeropuerto Chapelco (CPC).", "auto": "Ruta 40 y 237."}},
            # Tierra del Fuego
            {"province": "tierra-del-fuego", "name": "Ushuaia - Fin del Mundo", "slug": "ushuaia",
             "short_description": "La ciudad más austral del mundo: Canal Beagle, pingüinos y glaciares.",
             "description": "Ushuaia, conocida como la ciudad del Fin del Mundo, es la puerta de entrada a la Antártida. El Canal Beagle, la Isla de los Pájaros, el Parque Nacional Tierra del Fuego, el Tren del Fin del Mundo y las colonias de pingüinos la convierten en un destino único y emocionante.",
             "price_per_night": 100, "is_featured": True,
             "location_lat": -54.8019, "location_lng": -68.3030,
             "image": "https://images.unsplash.com/photo-1582827501715-e8e7c163a77a?w=600",
             "images": ["https://images.unsplash.com/photo-1582827501715-e8e7c163a77a?w=600"],
             "how_to_get": {"micro": "Desde Río Gallegos en 8h.", "avion": "Aeropuerto Ushuaia (USH)."}},
            # Santa Fe
            {"province": "santa-fe", "name": "Rosario", "slug": "rosario",
             "short_description": "La Chicago argentina: río Paraná, Monumento a la Bandera y cultura urbana.",
             "description": "Rosario es una ciudad portuaria vibrante a orillas del río Paraná. Su Monumento a la Bandera, el Parque de España, la costanera y la intensa vida cultural con museos, teatros y bares la convierten en un destino ideal para quienes buscan una experiencia urbana con río.",
             "price_per_night": 55, "is_featured": False,
             "location_lat": -32.9520, "location_lng": -60.6390,
             "image": "https://images.unsplash.com/photo-1599630640671-2c69e8c7a02e?w=600",
             "images": ["https://images.unsplash.com/photo-1599630640671-2c69e8c7a02e?w=600"],
             "how_to_get": {"micro": "Desde Retiro en 4h.", "avion": "Aeropuerto Rosario (ROS).", "tren": "Tren Rosario-Retiro."}},
        ]

        destinos = {}
        for dd in destinos_data:
            d, created = Destination.objects.update_or_create(
                slug=dd["slug"],
                defaults={
                    "province": provincias[dd["province"]],
                    "name": dd["name"],
                    "short_description": dd["short_description"],
                    "description": dd["description"],
                    "price_per_night": dd["price_per_night"],
                    "is_featured": dd["is_featured"],
                    "location_lat": dd["location_lat"],
                    "location_lng": dd["location_lng"],
                    "image": dd["image"],
                    "images": dd["images"],
                    "how_to_get": dd["how_to_get"],
                }
            )
            destinos[d.slug] = d
            if created:
                self.stdout.write(f"  Destino creado: {d.name}")

        # --- HOTELES ---
        hoteles_data = [
            {"dest": "caba", "name": "Alvear Palace Hotel", "rating": 4.9, "price": 350,
             "address": "Av. Alvear 1891, Recoleta", "phone": "011 4808-2100",
             "booking_url": "https://www.alvearpalace.com/",
             "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=400"},
            {"dest": "caba", "name": "Hotel Madero Buenos Aires", "rating": 4.7, "price": 180,
             "address": "Rosario Virrey del Pino 2452, Puerto Madero", "phone": "011 5776-9200",
             "booking_url": "https://www.hotelmadero.com/",
             "image": "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=400"},
            {"dest": "caba", "name": "Mine Hotel Boutique", "rating": 4.8, "price": 250,
             "address": "Gorriti 4770, Palermo Soho", "phone": "011 4832-2100",
             "booking_url": "https://www.minehotel.com/",
             "image": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=400"},
            {"dest": "caba", "name": "Howard Johnson Plaza", "rating": 4.5, "price": 120,
             "address": "Av. Callao 1180, Recoleta", "phone": "011 5353-2000",
             "booking_url": "https://www.howardjohnson.com/",
             "image": "https://images.unsplash.com/photo-1582719508461-905c673771fd?w=400"},
            {"dest": "mar-del-plata", "name": "NH Gran Hotel Provincial", "rating": 4.6, "price": 150,
             "address": "Av. Peralta Ramos 2500", "phone": "0223 499-7000",
             "booking_url": "https://www.nh-hotels.com/",
             "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=400"},
            {"dest": "mar-del-plata", "name": "Hotel Costa Galana", "rating": 4.8, "price": 200,
             "address": "Av. Frías 153", "phone": "0223 499-3000",
             "booking_url": "https://www.costagalana.com/",
             "image": "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=400"},
            {"dest": "salta-capital", "name": "Hotel Alejandro I", "rating": 4.7, "price": 120,
             "address": "Balcarce 252, Salta", "phone": "0387 431-4000",
             "booking_url": "https://www.hotelalejandro1.com/",
             "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=400"},
            {"dest": "salta-capital", "name": "Design Suites Salta", "rating": 4.6, "price": 100,
             "address": "Av. Reyes Católicos 1531", "phone": "0387 439-8000",
             "booking_url": "https://www.designsuites.com/",
             "image": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=400"},
            {"dest": "mendoza-capital", "name": "Park Hyatt Mendoza", "rating": 4.8, "price": 220,
             "address": "Chile 1124, Mendoza", "phone": "0261 441-1234",
             "booking_url": "https://www.hyatt.com/",
             "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=400"},
            {"dest": "mendoza-capital", "name": "Sheraton Mendoza", "rating": 4.5, "price": 160,
             "address": "Prilidiano Pueyrredón 175", "phone": "0261 441-6000",
             "booking_url": "https://www.marriott.com/",
             "image": "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=400"},
            {"dest": "bariloche", "name": "Llao Llao Hotel & Resort", "rating": 4.9, "price": 400,
             "address": "Av. Bustillo km 25", "phone": "0294 444-9000",
             "booking_url": "https://www.llaollao.com/",
             "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=400"},
            {"dest": "bariloche", "name": "Hotel Panamericano Bariloche", "rating": 4.6, "price": 180,
             "address": "Av. San Martín 536", "phone": "0294 443-6100",
             "booking_url": "https://www.panamericano.com/",
             "image": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=400"},
            {"dest": "cataratas-del-iguazu", "name": "Gran Meliá Iguazú", "rating": 4.8, "price": 300,
             "address": "Parque Nacional Iguazú", "phone": "03757 498-000",
             "booking_url": "https://www.melia.com/",
             "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=400"},
            {"dest": "cataratas-del-iguazu", "name": "Hotel Saint George", "rating": 4.4, "price": 120,
             "address": "Av. Córdoba 137, Puerto Iguazú", "phone": "03757 420-580",
             "booking_url": "https://www.hotelsaintgeorge.com/",
             "image": "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=400"},
            {"dest": "ushuaia", "name": "Los Cauquenes Resort", "rating": 4.7, "price": 280,
             "address": "Gobernador Paz 1785", "phone": "02901 444-400",
             "booking_url": "https://www.loscauquenes.com/",
             "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=400"},
            {"dest": "ushuaia", "name": "Hotel Alto Andino", "rating": 4.5, "price": 180,
             "address": "Av. Perito Moreno 2311", "phone": "02901 431-300",
             "booking_url": "https://www.altoandino.com/",
             "image": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=400"},
            {"dest": "villa-general-belgrano", "name": "Howard Johnson Villa General Belgrano", "rating": 4.3, "price": 90,
             "address": "Av. Julio A. Roca 150", "phone": "03546 461-000",
             "booking_url": "https://www.howardjohnson.com/",
             "image": "https://images.unsplash.com/photo-1582719508461-905c673771fd?w=400"},
            {"dest": "rosario", "name": "Pullman Rosario", "rating": 4.6, "price": 130,
             "address": "Av. Dorrego 245", "phone": "0341 530-8000",
             "booking_url": "https://www.pullmanhoteles.com/",
             "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=400"},
            {"dest": "san-martin-andes", "name": "Sol Arrayán Hotel & Spa", "rating": 4.7, "price": 160,
             "address": "Av. Koessler 775", "phone": "02972 427-400",
             "booking_url": "https://www.solarrayan.com/",
             "image": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=400"},
            {"dest": "quebrada-humahuaca", "name": "Hotel de Altura", "rating": 4.2, "price": 70,
             "address": "Belgrano 380, Tilcara", "phone": "0388 423-800",
             "booking_url": "https://www.hotelaltura.com/",
             "image": "https://images.unsplash.com/photo-1582719508461-905c673771fd?w=400"},
        ]

        for hd in hoteles_data:
            dest = destinos[hd["dest"]]
            hotel, created = Hotel.objects.get_or_create(
                name=hd["name"],
                destination=dest,
                defaults={
                    "rating": hd["rating"],
                    "price_per_night": hd["price"],
                    "address": hd["address"],
                    "phone": hd.get("phone", ""),
                    "booking_url": hd.get("booking_url", ""),
                    "image": hd.get("image", ""),
                }
            )
            if created:
                self.stdout.write(f"  Hotel creado: {hotel.name}")

        # --- RESEÑAS DE EJEMPLO ---
        user = User.objects.filter(username='viajero').first()
        if user:
            for dest_slug, rating, comment in [
                ("caba", 5, "¡Buenos Aires es increíble! La recomiendo muchísimo. La ciudad tiene una energía única."),
                ("bariloche", 5, "Bariloche es un paraíso. El Llao Llao es un hotel espectacular, las vistas al lago son impagables."),
                ("cataratas-del-iguazu", 5, "Las Cataratas son IMPACTANTES. Un destino obligatorio en Argentina. La Garganta del Diablo te deja sin aliento."),
                ("mendoza-capital", 4, "Mendoza tiene los mejores vinos del país. Las bodegas son hermosas y la gente es muy cálida."),
                ("salta-capital", 5, "Salta es una ciudad colonial preciosa. El tren a las nubes es una experiencia única."),
                ("ushuaia", 5, "Ushuaia es el fin del mundo pero el comienzo de todo. Paisajes que parecen de otro planeta."),
            ]:
                if dest_slug in destinos:
                    Review.objects.get_or_create(
                        destination=destinos[dest_slug],
                        user=user,
                        rating=rating,
                        defaults={"comment": comment}
                    )

        self.stdout.write(self.style.SUCCESS("¡Datos cargados exitosamente!"))
        self.stdout.write(f"  Provincias: {Province.objects.count()}")
        self.stdout.write(f"  Destinos: {Destination.objects.count()}")
        self.stdout.write(f"  Hoteles: {Hotel.objects.count()}")
        self.stdout.write(f"  Reseñas: {Review.objects.count()}")
        self.stdout.write("")
        self.stdout.write("Usuarios disponibles:")
        self.stdout.write("  Admin: admin / admin123")
        self.stdout.write("  Viajero: viajero / viajero123")
