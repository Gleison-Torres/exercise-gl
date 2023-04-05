# Generated by Django 4.1.4 on 2023-03-17 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login_register_user', '0005_alter_datauser_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datauser',
            name='user_profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]