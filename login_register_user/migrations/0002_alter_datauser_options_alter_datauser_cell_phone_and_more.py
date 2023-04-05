# Generated by Django 4.1.4 on 2023-03-10 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_register_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datauser',
            options={'verbose_name': 'Cadastro'},
        ),
        migrations.AlterField(
            model_name='datauser',
            name='cell_phone',
            field=models.CharField(blank=True, max_length=15, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='datauser',
            name='phone',
            field=models.CharField(blank=True, max_length=14, verbose_name='Telefone'),
        ),
    ]