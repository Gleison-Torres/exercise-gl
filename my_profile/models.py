from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):
    active = models.BooleanField('Ativo', default=True)
    create = models.DateField('Criado', auto_now_add=True)
    modified = models.DateField('Modificado', auto_now=True)

    class Meta:
        abstract = True


class AddressUser(Base):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    sender_name = models.CharField('Nome completo', max_length=100)
    postal_code = models.CharField('CEP', max_length=9)
    street_address = models.CharField('Rua/Avenida', max_length=200)
    number_address = models.CharField('Numero', max_length=20)
    additional_info = models.CharField('Complemento', max_length=200, blank=True)
    city = models.CharField('Cidade', max_length=100)
    state = models.CharField('Estado', max_length=2)

    TYPE_ADDRESS = (
        ('casa', 'Casa'),
        ('trabalho', 'Trabalho')
    )

    type_address = models.CharField(
        'Este é o seu trabalho ou sua casa?', max_length=8, choices=TYPE_ADDRESS, default=False
    )

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return self.sender_name

