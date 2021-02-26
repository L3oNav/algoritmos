import math

objectivo = int(input('Escoge un numero: '))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0
# |x| = abs()
while abs(respuesta**2 - objectivo ) >= epsilon and respuesta <= objectivo:
    respuesta += paso

if abs(respuesta**2 - objectivo) >= epsilon:
    print(f"No se encontro la raiz de: {objectivo}")
else:
    print(f"La raiz cuadrada de {objectivo} es {math.ceil(respuesta)}")


"""
math.round(numero, decimales)
x = math.round(5.7654, 2) -> 5.77
"""
