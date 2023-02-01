from pycep_correios import get_address_from_cep, WebService


adress = get_address_from_cep('08431999', webservice=WebService.APICEP)

print(f'Endereço: {adress}')