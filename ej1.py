def busqueda_lineal(lista, elemento):
    for i in range(len(lista)):

        if lista[i] == elemento:
            return i 
        
    return -1

elemento = int(input("Ingrese el Nº que desea buscar:"))
lista = [1,3,45,2,4,5]
resultado = busqueda_lineal(lista, elemento)
print(f"El elemento {elemento} esta en el indice: {resultado}")