"""
Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro
usando la primera función. formula area circulo = Pi*r**2 // volumen cilindro pi*(r**2)*h
"""
def areacirculo(radio):
    area=3.14*(radio**2)
    return area
def volumencilindro(area,altura):
    volumen=area*altura
    return volumen

def main():
    radio=float(input("Ingrese el radio: "))
    altura=float(input("Ingrese la altura"))
    area=areacirculo(radio)
    volumen=volumencilindro(area,altura)
    print(f"el area del circulo es {area} y el volumen de cilindro es {volumen}")

if __name__ == '__main__': 
    main()