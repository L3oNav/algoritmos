"""
list = [0,1,2,3,4,5,6,7,8,9,10]
"""

objectivo = int(input('Escoge un numero: '))
epsilon = 0.01
bajo = 0.0
alto = max(1.0, objectivo)
respuesta = (alto + bajo) / 2

while abs(respuesta**0.33-objectivo) >= epsilon:
    if respuesta**0.33<objectivo:
        bajo = respuesta
    else:
        alto = respuesta
    respuesta = (alto + bajo) / 2

print(f'La raiz cuadrada de {objectivo} es: {respuesta}')
