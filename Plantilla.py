

def operaciones():
    num1=int(input("ingrese el primer número:"))
    num2=int(input("ingrese el segundo número:"))
    suma=num1+num2
    resta=num1-num2
    multiplicación=num1*num2
    división=num1/num2
    if num2==0:
        print(f"La suma es={suma},\nLa resta es= {resta},"
          f"\nLa multiplicación es={multiplicación},"
          f"\ndivisión no se puede dividir entre cero,")
    else:
        print(f"La suma es={suma},\nLa resta es={resta},"
          f"\nLa multiplicación es={multiplicación},"
          f"\nLa división es={división}")
              
              
              


