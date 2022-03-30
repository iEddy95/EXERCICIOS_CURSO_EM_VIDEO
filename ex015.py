dias = int(input('Quantos dias ficou alugado? '))
km = float(input('Quantos Km rodados?'))
pg = (km * 0.15) + (dias * 60)
print(f'O total a pagar é de R${pg}')