#IMPLEMENTAMOS LA RESTA
nu1 = float(input())
nu2 = float(input())
result = nu1 - nu2

print(result)

#IMPLEMENTAMOS MULTIPLICACIÓN
num1 = 5
num2 = 4

resultado = num1 * num2

print(resultado)

#IMPLEMENTAMOS LA DIVISIÓN
nume1 = 20
nume2 = 5

resultado = nume1 / nume2

print(resultado)

#IMPLEMENTAMOS OPERADOR MÓDULO (%)
numer1 = 10
numer2 = 3

resultado = numer1 % numer2

print(resultado)

#IMPLEMENTAMOS EL PERMITIR ELEGIR LA OPERACIÓN
numero1 = float(input())
numero2 = float(input())
operacion = input()

if operacion == "+":
    resultado = numero1 + numero2

elif operacion == "-":
    resultado = numero1 - numero2

elif operacion == "*":
    resultado = numero1 * numero2

elif operacion == "/":
    resultado = numero1 / numero2

#IMPLEMENTAMOS SUMA DE 3 NÚMEROS
numero1 = float(input())
numero2 = float(input())
numero3 = float(input())

resultado = numero1 + numero2 + numero3

print(resultado)

#IMPLEMENTAMOS EL MEZCLAR OPERACIONES CON 3 NÚMEROS O MÁS
#Usamos eval() que permite evaluar una expresión matemática escrita como
operacion = input()

resultado = eval(operacion)

print(resultado)