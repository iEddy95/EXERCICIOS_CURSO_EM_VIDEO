import math
ang = float(input('Digite um angulo: '))
s = math.sin(math.radians(ang))
c = math.cos(math.radians(ang))
t = math.tan(math.radians(ang))

print(f'O seno de {ang} é {s:.2f}')
print(f'O scosseno de {ang} é {c:.2f}')
print(f'O seno de {ang} é {t:.2f}')