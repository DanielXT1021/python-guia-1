"""
Cree un programa conversor de unidades, donde muestre una serie de unidades a convertir y la
opción de terminar el programa. Si se selecciona la opción de terminar el programa, se debe
terminar la ejecución del mismo. Por ejemplo:
a. ¿Que conversión desea realizar?
b. 1) centímetros --> pulgadas
c. 2) metros --> kilometros
d. 3) onzas --> gramos
e. 4) milla --> kilometro
f. 5) celcius --> fahrenheit
g. 6) Salir
"""
def main():
    salir=False
    while salir==False:
        opcion=int(input("\n¿Que conversión desea realizar?\n\n1) centímetros --> pulgadas\n2) metros --> kilometros\n3) onzas --> gramos\n4) milla --> kilometro\n5) celcius --> fahrenheit\n6) Salir\n\n Elije alguna opcion del 1 al 6: "))
        if opcion==1:
            print("\nConversion de Centimetros a Pulgadas")
            centimetros=float(input("Ingrese la cantidad de centimetros a convertir: "))
            pulgadas=centimetros/2.54
            print(f"La conversion de {centimetros}cm a pulgadas es: {pulgadas}")
        if opcion==2:
            print("\nConversion de metros --> kilometros")
            metros=float(input("Ingrese la cantidad de metros a convertir: "))
            kilometros=metros/1000
            print(f"La conversion de {metros}mts a kilometros es: {kilometros}")
        if opcion==3:
            print("\nConversion de onzas --> gramos")
            onzas=float(input("Ingrese la cantidad de onzas a convertir: "))
            gramos=onzas*28.35
            print(f"La conversion de {onzas}Oz a gramos es: {gramos}")
        if opcion==4:
            print("\nConversion de milla --> kilometro")
            millas=float(input("Ingrese la cantidad de metros a convertir: "))
            kilometros=millas*1.609
            print(f"La conversion de {millas}millas a kilometros es: {kilometros}")
        if opcion==5:
            print("\nConversion de celcius --> fahrenheit")
            celcius=float(input("Ingrese la cantidad de celcius a convertir: "))
            fahrenheit=(celcius*(9/5))+32
            print(f"La conversion de {celcius}° Celcius a fahrenheit es: {fahrenheit}")
        if opcion==6:
            salir=True
    print("has salido del sistema")
if __name__ == '__main__':
    main() 
