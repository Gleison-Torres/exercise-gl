# Generated by Django 4.1.4 on 2023-03-12 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_register_user', '0003_remove_datauser_phone_alter_datauser_cell_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datauser',
            old_name='user',
            new_name='user_profile',
        ),
    ]
