nome = str(input('Quan seu nome? ')).strip()

print(f'Seu nome em minúsculo: {nome.lower()}')
print(f'Seu nome em maiusculo: {nome.upper()}')
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu nome tem {} letras.'.format(nome.find(' ')))
separar = nome.split()
print('Seu primeiro nome é {} e tem {} letras.'.format(separar[0], len(separar[0])))