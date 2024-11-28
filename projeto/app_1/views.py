from django.shortcuts import render
from .models import Hotel, Quarto

def lista_hotels(request):
    hotels = Hotel.objects.all()
    return render(request, 'index.html', {'hotels': hotels})

def detalhes_hotel(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)
    quartos = hotel.quartos.all()
    return render(request, 'detalhes_hotel.html', {'hotel': hotel, 'quartos': quartos})

# app_1/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Hotel, Quarto,Reserva
from .forms import ReservaForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def reservar_quarto(request, quarto_id):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.quarto_id = quarto_id
            reserva.cliente = request.user  # Associando o usuário logado à reserva
            reserva.save()
            return redirect('confirmacao_reserva', reserva_id=reserva.id)
    else:
        form = ReservaForm()

    context = {'form': form, 'quarto': Quarto.objects.get(id=quarto_id)}
    return render(request, 'reservar_quarto.html', context)


def confirmacao_reserva(request, reserva_id):
    reserva = Reserva.objects.get(id=reserva_id)
    return render(request, 'confirmacao_reserva.html', {'reserva': reserva})

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Faz login automaticamente após o cadastro
            return redirect('index')  # Redireciona para a lista de hotéis
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})


from django.contrib.auth.decorators import login_required
from .models import Reserva

@login_required
def minhas_reservas(request):
    reservas = Reserva.objects.filter(cliente=request.user)  # Filtra as reservas pelo usuário logado
    return render(request, 'minhas_reservas.html', {'reservas': reservas})

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Reserva

@login_required
def cancelar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id, cliente=request.user)
    if request.method == 'POST':
        reserva.delete()
        messages.success(request, "Reserva cancelada com sucesso.")
        return redirect('minhas_reservas')
    return render(request, 'cancelar_reserva.html', {'reserva': reserva})
