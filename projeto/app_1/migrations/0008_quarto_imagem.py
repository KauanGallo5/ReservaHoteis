# Generated by Django 5.1.3 on 2024-11-09 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0007_reserva_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='quarto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='quartos/'),
        ),
    ]
