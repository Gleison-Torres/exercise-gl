# Generated by Django 4.1.4 on 2023-02-14 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0002_alter_addressuser_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressuser',
            name='neighborhood',
            field=models.CharField(default=True, max_length=100, verbose_name='Bairro'),
        ),
    ]