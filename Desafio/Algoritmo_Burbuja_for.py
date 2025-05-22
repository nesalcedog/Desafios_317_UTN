
## Ordenamiento de lista metodo burbuja con for :)

lista = [54, 34, 25, 12, 22, 11, 90]

n = len(lista)

for i in range(len(lista)):
    intercambio = False
    for j in range(n - 1 - i):
            if lista[j] > lista [j + 1]: ##Si j es mayor a la posicion siguiente
                temp = lista [j] #me guardo temporalmente a j
                lista[j] = lista[j + 1] #intercambio los valores
                lista[j + 1] = temp
                intercambio = True
    if not intercambio:
        break

    
    
print(lista)


