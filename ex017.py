import math
cop = float(input('Comprimento do cateto oposto: '))
cadj = float(input('Comprimento do cateto adjacente: '))
hip = math.hypot(cop, cadj)

print(f'A hipotenusa do triangulo vale: {hip:.2f}')