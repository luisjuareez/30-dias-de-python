#LEVEL 1
edad = input('Intoduzca su edad:')
edad_para_conducir= int(18)
if int(edad) >= int(18):
    print('Tienes edad para conducir')
años_faltan_conducir= edad_para_conducir - int(edad)
if int(edad) < int(18) : 
    print('todavía no tienes edad de conducir', 'Tienes que esperar', años_faltan_conducir, 'años más')

print('¿Quién es mayor tú o yo?')
tu_edad = input('Ingresa tu edad:') 
mi_edad = int(16)
if int(tu_edad) > int(16):
    diferencia_edad= int(tu_edad) - int(16)
    print('Eres', diferencia_edad, 'años mayor que yo')
if int(tu_edad) == int(16): 
    print('Tenemos la misma edad!!!')
else:
    diferencia_edad= int(16) - int(tu_edad)
    print('Eres', diferencia_edad,  'años más pequeño que yo')

a = input('Intoduce un número:')
b = input('Introduce otro número:')
if int(a) > int(b): 
    print('El número', int(a), 'es mayor que el número', int(b))
if int(a) < int(b): 
    print('El número', int(a), 'es menor que el número', int(b))
if int(a) == int(b):
    print('Ambos números son iguales')
#LEVEL 2

nota= input('Introduce tu nota:')
A= 100/90
B= 70/89
C= 60/69
D= 50/59
F= 0/49
if int(nota) > int(80) and int(nota) < int(100):
    print('Tras tu nota de', int(nota), ', tu calificación es de', int(A))
elif int(nota) > int(70) and int(nota) < int(89):
    print('Tras tu nota de', int(nota), ', tu calificación es de', int(B))
elif int(nota) > int(60) and int(nota) < int(79): 
    print('Tras tu nota de', int(nota), ', tu calificación es de', int(C))
elif int(nota) > int(50) and int(nota) < int(59):
    print('Tras tu nota de', int(nota), ', tu calificación es de', int(D))
elif int(nota) > int(0) and int(nota) < int(49):
    print('Tras tu nota de', int(nota), ', tu calificación es de', int(F))