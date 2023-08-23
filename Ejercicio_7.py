"""
Escriba un programa que calcule el factorial de un número ingresado por el usuario.
"""
def main():
    numeroing=int(input("Ingrese u numero: "))
    factorial=1
    suma=0
    for i in range(numeroing,0,-1):
        factorial=factorial*i
    print(f"el factorial de {numeroing} es: {factorial}")

if __name__ == '__main__': 
    main()

