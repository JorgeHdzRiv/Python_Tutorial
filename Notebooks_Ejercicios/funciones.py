def suma_dos(n1,n2):
    print(f"El total de la suma es: {n1+n2}")

def promedio_numeros(*numeros):
    acum = 0
    for num in numeros:
        acum += num
    print(f"El promedio de los numeros es: {acum/(len(numeros))}") 

def nombres(nombres):
    for nombre in nombres:
        print(nombre)


