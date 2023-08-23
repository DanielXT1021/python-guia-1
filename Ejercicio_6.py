"""
Escriba un programa que pida al usuario una palabra y la imprima al revés. El programa debe
continuar pidiendo palabras hasta que el usuario ingrese "salir";.
"""
def main():
    salir=False

    while salir==False:
        palabra=input("Ingrese la palabra: ")
        if palabra.lower()=="salir":
            salir=True
        else:
            print(f"Palabra al reves {palabra[::-1]}")
    print("Saliste del programa")


if __name__ == '__main__': 
    main()