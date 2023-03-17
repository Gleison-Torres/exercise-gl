from django import forms
from .models import AddressUser


class AddressForm(forms.ModelForm):
    class Meta:
        model = AddressUser
        fields = (
            'sender_name', 'postal_code', 'street_address',
            'number_address', 'neighborhood', 'additional_info', 'city', 'state', 'type_address', 'active'
        )

        widgets = {
            'type_address': forms.RadioSelect,
            'city': forms.TextInput(attrs={'readonly': True}),
            'state': forms.TextInput(attrs={'readonly': True}),
        }
