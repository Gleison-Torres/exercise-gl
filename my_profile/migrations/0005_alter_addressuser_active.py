# Generated by Django 4.1.4 on 2023-03-03 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0004_alter_addressuser_neighborhood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressuser',
            name='active',
            field=models.BooleanField(verbose_name='Ativo'),
        ),
    ]