#Day 2: 30 Days of python programming

first_name ='Luis'
last_name ='Juarez'
full_name ='Luis Juarez'
country ='Spain'
city ='Jerez'
age ='16'
year ='2022'
is_married ='True'
is_true ='False'
is_light_on ='Yes'
first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on ='Luis', 'Juarez', 'Luis Juarez', 'Spain', 'Jerez', '16', '2022', 'True', 'False', 'Yes'

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))
print(len(first_name==last_name))

num_one='5'
num_two='4'

cuenta_1 = num_one + num_two
print('Suma', cuenta_1)
cuenta_2 = num_one - num_two
print('Resta', cuenta_2)
cuenta_3 = num_one * num_two
print('Multiplicación', cuenta_3)
cuenta_4 = num_one / num_two
print('División', cuenta_4)
cuenta_5 = num_one//num_two
print('División del piso',cuenta_5)
cuenta_6 = num_one ** num_two
print('Potencia', cuenta_6)

radio= 30 
area_de_circulo = 3.14 *radio**2 
print('Área d un circulo', area_de_circulo)
circunferencia_de_circulo = 3.14 * radio 
print('Circunfernecia', circunferencia_de_circulo)

r =input ("¿Cual es el radio")
r2 = int(r)
area = 3.14 * r2 ** 2
print(area)

help('keywords')
