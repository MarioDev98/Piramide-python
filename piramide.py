def triangulo(numero):
    for i in range(1, numero+1):
        print("*" * i)

numero = int(input("Introduce un número: "))
triangulo(numero)