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

if __name__ == '__main__': #Punto de entrada
    main() 