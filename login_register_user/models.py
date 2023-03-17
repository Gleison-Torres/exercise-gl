from django.db import models
from django.contrib.auth.models import User


class DataUser(models.Model):
    objects = None
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    cell_phone = models.CharField('Telefone', max_length=15, blank=True)
    cpf = models.CharField('CPF', max_length=14)

    class Meta:
        verbose_name = 'Cadastro'
        



'''www.vemsertp.com.br

recrutamento.teleperformance.com.br'''