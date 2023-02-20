from django.contrib import admin
from . import models


@admin.register(models.AddressUser)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'type_address', 'street_address', 'city', 'state', 'active')

