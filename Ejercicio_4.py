"""
Escriba un programa que pida dos palabras y diga si riman o no. Si coinciden las últimas tres
letras tiene que decir que riman. Si coinciden sólo las últimas dos tiene que decir que riman un
poco. Y si no coinciden, decir que no riman. Validar que las palabras tengan al menos tres letras.
Nota: Utilizar slices.
"""
def main():
    
    palabra1 = input("Ingresa la primera palabra: ")
    palabra2 = input("Ingresa la segunda palabra: ")

    if len(palabra1) < 3 or len(palabra2) < 3:
        print("Eso no se puede verificar muy cortooooooooo... Gracias :)")
    if palabra1[-3:] == palabra2[-3:]:
        print("Si que rima eso")
    elif palabra1[-2:] == palabra2[-2:]:
        print("Ya casi rima")
    else:
        print("Definitivamente no es lo tuyo no rima")
if __name__ == '__main__': 
    main() 