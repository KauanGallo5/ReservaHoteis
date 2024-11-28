from django import forms
from .models import Reserva, Quarto

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['data_check_in', 'data_check_out']
        widgets = {
            'data_check_in': forms.DateInput(attrs={'type': 'date'}),
            'data_check_out': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'initial' in kwargs:
            kwargs['initial']['nome_cliente'] = kwargs['initial'].get('nome_cliente', None) or kwargs.get('user').username
            kwargs['initial']['email_cliente'] = kwargs['initial'].get('email_cliente', None) or kwargs.get('user').email
