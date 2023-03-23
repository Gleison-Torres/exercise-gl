from django.contrib import admin
from . import models


@admin.register(models.DataUser)
class DataUserAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'cell_phone', 'cpf')
