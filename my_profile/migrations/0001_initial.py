# Generated by Django 4.1.4 on 2023-02-04 22:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('create', models.DateField(auto_now_add=True, verbose_name='Criado')),
                ('modified', models.DateField(auto_now=True, verbose_name='Modificado')),
                ('sender_name', models.CharField(max_length=100, verbose_name='Nome completo')),
                ('postal_code', models.CharField(max_length=9, verbose_name='CEP')),
                ('street_address', models.CharField(max_length=200, verbose_name='Rua/Avenida')),
                ('number_address', models.CharField(max_length=20, verbose_name='Numero')),
                ('additional_info', models.CharField(blank=True, max_length=200, verbose_name='Complemento')),
                ('city', models.CharField(max_length=100, verbose_name='Cidade')),
                ('state', models.CharField(max_length=2, verbose_name='Estado')),
                ('type_address', models.CharField(choices=[('casa', 'Casa'), ('trabalho', 'Trabalho')], max_length=8, verbose_name='Este é o seu trabalho ou sua casa?')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Endereço',
            },
        ),
    ]
