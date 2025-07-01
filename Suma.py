def suma(a, b):
    return a + b

while True:
 try:

    l1 = int(input("Ingrese el primer número: "))
    l2 = int(input("Ingrese el segundo número: "))
 except:
    print("Ingrese numero enteros")  
    break 
resultado = suma(l1,l2)
print(resultado)