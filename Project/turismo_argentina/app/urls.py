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
    path('resena/<int:review_id>/editar/', views.edit_review, name='edit_review'),
    path('resena/<int:review_id>/eliminar/', views.delete_review, name='delete_review'),
    path('geolocalizacion/',views.geolocalizacion, name='Geolocalizacion'),
    path('panel/', views.admin_panel, name='admin_panel'),
    path('panel/provincia/<slug:slug>/editar/', views.admin_edit_province, name='admin_edit_province'),
    path('panel/destino/<slug:slug>/editar/', views.admin_edit_destination, name='admin_edit_destination'),
]
