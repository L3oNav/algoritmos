objectivo = int(input('Escoge un entero: '))
respuesta = 0

while respuesta**2 < objectivo:
    respuesta += 1

if respuesta**2 == objectivo:
    print(f'La raiz cuadrada de {objectivo} es {respuesta}')
else:
    print(f'{objectivo} no tiene una raiz cuadrada exacta')
