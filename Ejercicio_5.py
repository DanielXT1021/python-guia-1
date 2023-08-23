"""
Escribe un programa que le pida al usuario una palabra y una letra. El programa debe contar
cuántas veces aparece la letra en la palabra usando un ciclo for.
"""
def main():
    Palabra=input("Ingrese una palabra: ")
    letra=input("Ingrese una letra: ")
    largo=len(Palabra)
    contador=0
    for i in range(0,largo):
        if Palabra[i]==letra:
            contador+=1
    print(f"La letra {letra} se repite {contador}")
if __name__ == '__main__': 
    main()