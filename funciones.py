
#<# 1- Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

"""
Sin parametro
"""

# def numero_entero():
#     numero = int(input("Ingrese un numero: "))    
#     return numero

# num = numero_entero()
# print(f"El numero ingresado es {num}")

"""
Con parametro
"""
""" ESTA MAL ECHO PORQUE SE TIENE QUE PEDIR DENTRO DE LA FUNCION
numero = int(input("Ingrese un numero: "))

def numero_entero(numero):
    print(f"El numero ingresado es {numero}")
    
numero_entero(numero) 
"""

## 2 - Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

# def numero_flotante():
#     numero = float(input("Ingrese un numero flotante: "))    
#     return numero

# num = numero_flotante()
# print(f"El numero ingresado es {num}")

## 3 - Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 

# def cadena():
#     oracion = input("Ingrese una cadena de texto: ")
    
#     return oracion

# texto = cadena()
# print(texto)

# 4 - Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 

# def area_rectangulo(base, altura):
    
#     area = base * altura
    
#     return area

# base = 5
# altura = 10

# rectangulo = area_rectangulo(base, altura)
# print(rectangulo)

# def rectangulo_area():
    
#     altura = int(input("Ingrese la altura del rectangulo: "))
#     base = int(input("Ingrese la base del rectangulo: "))
    
#     area = altura * base
    
#     return area

# resultado = rectangulo_area()
# print(f"El area del rectangulo es {resultado}")

# 5 - Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

# def area_circulo(radio):
    
#     area = 3.14 * radio * radio
    
#     return area

# radio = 2

# circulo = area_circulo(radio)
# print (f"El area del circulo es {circulo}")

# # 6 Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.

# def numero():
    
#     mensaje = int(input("Ingrese un numero: "))
    
#     if mensaje % 2 == 0:
#         print(f"Tu numero es par")
    
#     else:
#         print(f"Tu numero es impar")
    
#     return mensaje

# message = numero()

# # 7 Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.

# def numero():
    
#     mensaje = int(input("Ingrese un numero: "))
    
#     cuenta = mensaje % 2 == 0
        
#     return cuenta

# message = numero()
# print(message)

# # 8 Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

# def numero_mayor(a, b, c):
#     mayor = 0
#     lista = a,b,c
    
#     for i in lista:
#         if i > mayor:
#             mayor = i
           
#     print (f"El numero mayor es {mayor}")   
#     return mayor    

# a = 32
# b = 21
# c = 11

# numero_mayor(a,b,c)


# # 9 Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

def potencia(a, b):
    
    numero = a ** b 
    
    resultado = numero
    
    return resultado

a = 8
b = 2
potenciacion = potencia(a,b)
print (potenciacion)
    
# # 10 Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.


