from django import forms
from .models import AddressUser


class AddressForm(forms.ModelForm):
    class Meta:
        model = AddressUser
        fields = (
            'sender_name', 'postal_code', 'street_address',
            'number_address', 'additional_info', 'city', 'state', 'type_address'
        )

        widgets = {
            'type_address': forms.RadioSelect
        }
