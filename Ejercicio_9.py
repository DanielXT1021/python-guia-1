"""
Escribir un programa que contenga una función que reciba una lista de palabras y devuelva la
palabra más larga. Imprimir por pantalla la palabra resultante.
"""

def palabramaslarga(listapalab):
    palabramaslarga = ""
    for palabra in listapalab:
        if len(palabra) > len(palabramaslarga):
            palabramaslarga = palabra
    return palabramaslarga

def main():

    numpalabras = int(input("Cuantas palabras ingresaras: "))
    listapalab = []
    for i in range(numpalabras):
        palabra = input("Ingresa una palabra: ")
        listapalab.append(palabra)

    palabralarga = palabramaslarga(listapalab)
    print(f"La palabras mas larga es: {palabralarga}")

if __name__ == '__main__': 
    main()