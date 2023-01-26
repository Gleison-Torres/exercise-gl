variavel = 'ContEudo./'
count_upper = 0
count_char_special = 0


for digito in variavel:
    if digito.isupper():
        count_upper += 1

    if digito in '#@$%¨&*()<>?.,/':
        count_char_special += 1

print(f'Numero de letras maiúsculas: {count_upper} e {count_char_special} caracteres especiais.')
