print('ola mundo')
nu = []
for c in range(1, 5):
    n = int(input(f'\033[31mdigite o {c}° numero:'))
    nu.append(n)
print(f'menor numero foi {min(nu)}')