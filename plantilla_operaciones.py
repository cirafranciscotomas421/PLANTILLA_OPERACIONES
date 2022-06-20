import Plantilla
while True:
    Plantilla.operaciones()
    condicion= input("¿Desea introducir otro número? (S=si N=no):")
    if condicion == "n" or condicion == "N":
        break
print("fin de la calculadora")

