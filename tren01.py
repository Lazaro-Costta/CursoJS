dados = {'nome':'', 'media':'' }
dados['nome'] = str(input('Nome:'))
dados['media'] = float(input(f'media de {dados['nome']}:'))
print(f'o nome é igual a {dados['nome']}')
print(f'a media é igual a {dados["media"]}')
if dados['media'] < 6.5:
    print('REPROVADO')
else:
    print('APROVADO')