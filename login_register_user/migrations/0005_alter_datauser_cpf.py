# Generated by Django 4.1.4 on 2023-03-17 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_register_user', '0004_rename_user_datauser_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datauser',
            name='cpf',
            field=models.CharField(max_length=14, unique=True, verbose_name='CPF'),
        ),
    ]
