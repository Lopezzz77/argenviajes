from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Avg, Q
from .models import Province, Destination, Hotel, Review


def index(request):
    provinces = Province.objects.all()
    featured = Destination.objects.filter(is_featured=True)[:6]
    regions = Province.objects.values_list('region', flat=True).distinct()
    context = {
        'provinces': provinces,
        'featured': featured,
        'regions': regions,
    }
    return render(request, 'app/index.html', context)


def search(request):
    q = request.GET.get('q', '')
    region = request.GET.get('region', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')

    results = Destination.objects.all()

    if q:
        results = results.filter(
            Q(name__icontains=q) |
            Q(description__icontains=q) |
            Q(province__name__icontains=q)
        )

    if region:
        results = results.filter(province__region=region)

    if min_price:
        results = results.filter(price_per_night__gte=min_price)

    if max_price:
        results = results.filter(price_per_night__lte=max_price)

    regions = Province.objects.values_list('region', flat=True).distinct()
    return render(request, 'app/search.html', {
        'results': results,
        'query': q,
        'regions': regions,
        'selected_region': region,
        'min_price': min_price,
        'max_price': max_price,
    })


def province_detail(request, slug):
    province = get_object_or_404(Province, slug=slug)
    destinations = province.destinations.all()
    return render(request, 'app/province_detail.html', {
        'province': province,
        'destinations': destinations,
    })


def destination_detail(request, slug):
    destination = get_object_or_404(Destination, slug=slug)
    hotels = destination.hotels.all().order_by('-rating')
    reviews = destination.reviews.all().order_by('-created_at')
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    return render(request, 'app/destination_detail.html', {
        'destination': destination,
        'hotels': hotels,
        'reviews': reviews,
        'avg_rating': round(avg_rating, 1),
    })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})


@login_required
def add_review(request, slug):
    destination = get_object_or_404(Destination, slug=slug)
    if request.method == 'POST':
        rating = int(request.POST.get('rating', 5))
        comment = request.POST.get('comment', '')
        Review.objects.create(
            destination=destination,
            user=request.user,
            rating=rating,
            comment=comment,
        )
    return redirect('destination_detail', slug=slug)


# ==========================================
# 📍 MÓDULO DE GEOLOCALIZACIÓN Y TRIANGULACIÓN
# ==========================================

# Coordenadas fijas de las 3 antenas de referencia
PUNTO_A = {'x': 0, 'y': 0}
PUNTO_B = {'x': 100, 'y': 0}
PUNTO_C = {'x': 50, 'y': 86.6}


@login_required
def geolocalizacion(request):
    resultado = None

    if request.method == 'POST':
        try:
            distancia_a = float(request.POST.get('distancia_a', 0))
            distancia_b = float(request.POST.get('distancia_b', 0))
            distancia_c = float(request.POST.get('distancia_c', 0))
        except (TypeError, ValueError):
            distancia_a = distancia_b = distancia_c = 0

        # Algoritmo de trilateración para calcular ubicación aproximada
        x = (distancia_a ** 2 - distancia_b ** 2 + PUNTO_B['x'] ** 2) / (2 * PUNTO_B['x'])
        y = (
            distancia_a ** 2 - distancia_c ** 2
            + PUNTO_C['x'] ** 2 + PUNTO_C['y'] ** 2
            - 2 * PUNTO_C['x'] * x
        ) / (2 * PUNTO_C['y'])

        resultado = {'x': round(x, 2), 'y': round(y, 2)}

    return render(request, 'app/geolocalizacion.html', {
        'punto_a': PUNTO_A,
        'punto_b': PUNTO_B,
        'punto_c': PUNTO_C,
        'resultado': resultado,
    })