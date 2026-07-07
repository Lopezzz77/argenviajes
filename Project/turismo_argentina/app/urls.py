from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar/', views.search, name='search'),
    path('provincia/<slug:slug>/', views.province_detail, name='province_detail'),
    path('destino/<slug:slug>/', views.destination_detail, name='destination_detail'),
    path('registro/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('destino/<slug:slug>/resena/', views.add_review, name='add_review'),
    path('geolocalizacion/',views.geolocalizacion, name='Geolocalizacion'),
]
