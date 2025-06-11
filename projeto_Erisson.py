print('fassa seu cadrasto')
lista = []
while True:
    nome = str(input(f'digite seu nome:'))
    lista.append(nome)
    idade = int(input(f'digite sua idade:'))
    lista.append(idade)
    continuar = str(input('quer continuar:'))[0].upper()
    if continuar == 'N':
        break
print(f'{lista}')