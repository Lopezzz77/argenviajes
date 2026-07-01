from django.db import models
from django.contrib.auth.models import User

class Province(models.Model):
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(blank=True, help_text="URL de imagen representativa")
    region = models.CharField(max_length=50, choices=[
        ('norte', 'Norte'),
        ('cuyo', 'Cuyo'),
        ('centro', 'Centro'),
        ('patagonia', 'Patagonia'),
        ('litoral', 'Litoral'),
        ('bsas', 'Buenos Aires'),
    ])
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"

    def __str__(self):
        return self.name


class Destination(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='destinations')
    name = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.CharField(max_length=300)
    image = models.URLField(blank=True)
    images = models.JSONField(default=list, blank=True, help_text="Lista de URLs de imágenes")
    location_lat = models.FloatField(help_text="Latitud para Google Maps")
    location_lng = models.FloatField(help_text="Longitud para Google Maps")
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    how_to_get = models.JSONField(default=dict, blank=True, help_text='{"micro": "...", "avion": "...", "tren": "..."}')
    is_featured = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Destino"
        verbose_name_plural = "Destinos"

    def __str__(self):
        return f"{self.name} - {self.province.name}"


class Hotel(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='hotels')
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField(blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=50, blank=True)
    booking_url = models.URLField(blank=True, help_text="URL de reserva")

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hoteles"

    def __str__(self):
        return self.name


class Review(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Reseña"
        verbose_name_plural = "Reseñas"

    def __str__(self):
        return f"{self.user.username} - {self.destination.name} ({self.rating}/5)"
