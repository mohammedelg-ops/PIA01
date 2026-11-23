# Problema 1. Procesamiento de una lista de enteros


def procesar_lista(numeros):
    # 1. Quitar los numeros negativos
    positivos = []
    for n in numeros:
        if n >= 0:
            positivos.append(n)

    # 2. Quitar los repetidos (un set no admite duplicados)
    sin_repetidos = set(positivos)

    # 3. Ordenar de menor a mayor
    resultado = sorted(sin_repetidos)
    return resultado


# Prueba
lista = [4, -1, 2, 4, 3, -5, 2]
print("Lista original:", lista)
print("Resultado:", procesar_lista(lista))

lista2 = [10, -3, 0, 7, 7, -8, 1, 10]
print("Lista original:", lista2)
print("Resultado:", procesar_lista(lista2))
