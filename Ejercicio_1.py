
""""
Cree un programa que elija un numero al azar entre 1 y 100, luego le pregunta por un número y
el programa le debe decir si el numero ingresado es demasiado bajo o demasiado alto, hasta
que logre dar con el numero generado.

"""

import random

def main():
    
    NumeroAzar=random.randint(1,100)
    Acerto=False
    while (Acerto==False):
        NumeroEsc=int(input("Ingrese un numero del 1 al 100:"))
        if NumeroEsc>NumeroAzar:
            print("El numero ingresado es muy alto")
        if NumeroEsc<NumeroAzar:
            print("El numero ingresado es muy bajo")
        if NumeroEsc==NumeroAzar:
            Acerto=True
    print("Felicidades no eras tan malo a pesar de todo :)")

if __name__ == '__main__': 
    main() 