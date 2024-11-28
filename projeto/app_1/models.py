from django.db import models

class Hotel(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    imagem = models.ImageField(upload_to='hotels/', null=True, blank=True)
    
    def __str__(self):
        return self.nome

class Quarto(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='quartos')
    numero = models.IntegerField()
    descricao = models.TextField()
    capacidade = models.IntegerField()
    diaria = models.DecimalField(max_digits=8, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='quartos/', blank=True, null=True)  # Novo campo para imagem

    def __str__(self):
        return f"Quarto {self.numero} - {self.hotel.nome}"
    def is_disponivel(self, data_check_in, data_check_out):
        """Verifica se o quarto está disponível nas datas especificadas.

        Args:
            data_check_in (date): Data de check-in.
            data_check_out (date): Data de check-out.

        Returns:
            bool: True se o quarto estiver disponível, False caso contrário.
        """

        reservas = self.reservas.filter(
            data_check_in__lte=data_check_out,
            data_check_out__gte=data_check_in
        )
        return not reservas.exists()

from django.contrib.auth.models import User

class Reserva(models.Model):
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE, related_name='reservas')
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)  # Relacionamento com o User
    nome_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    data_check_in = models.DateField()
    data_check_out = models.DateField()
    data_reserva = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Calcula o número de noites
        num_noites = (self.data_check_out - self.data_check_in).days
        self.valor_total = num_noites * self.quarto.diaria
        super(Reserva, self).save(*args, **kwargs)

    def __str__(self):
        return f"Reserva de {self.nome_cliente} para o Quarto {self.quarto.numero}"
