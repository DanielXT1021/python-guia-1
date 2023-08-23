"""
Cree un programa que solicite al usuario un número y determine si el número es primo o no.
"""
def main():
    numeroing=int(input("Ingrese un numero"))
    n=0
    for i in range(2,numeroing+1):
        for j in range(1,i+1):
            VerificarPrimo=True
            resto=i%j
            if resto==0 and j!=1 and j!=i:
                VerificarPrimo=False
                break
    if(VerificarPrimo==True):
        print("El numero ingresado es primo")
    else:
        print("El numero ingresado no es primo")
if __name__ == '__main__': 
    main() 
