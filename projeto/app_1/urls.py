from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.lista_hotels, name='index'),
    path('hotel/<int:hotel_id>/', views.detalhes_hotel, name='detalhes_hotel'),
    path('reservar/quarto/<int:quarto_id>/', views.reservar_quarto, name='reservar_quarto'),
    path('confirmacao_reserva/<int:reserva_id>/', views.confirmacao_reserva, name='confirmacao_reserva'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('minhas_reservas/', views.minhas_reservas, name='minhas_reservas'),
    path('cancelar_reserva/<int:reserva_id>/', views.cancelar_reserva, name='cancelar_reserva'),
]
