def sumar (a,b):
    return a + b
def restar (a,b):
    return a - b
def multiplicar (a,b):
    return a*b
def dividir (a,b):
    return a/b

print ("Hola, como estas\n")
a1 = float (input("Ingresa la primera cifra\n"))
operacion = input ("Ingrese la operacion\n[+]Sumar\n[-]Restar\n[*]Multiplicar\n[/]Dividir\n")
b2 = float (input("Ingrese el segundo numero\n"))
if operacion == "+" :
    print (sumar (a1,b2))
elif operacion == "-":
    print (restar(a1,b2))
elif operacion == "*":
    print (multiplicar(a1,b2))
elif operacion == "/":
    print (dividir(a1,b2))