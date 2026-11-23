# Problema 3. Trabajo con conjuntos


def operaciones_conjuntos(lista1, lista2):
    # Pasar las listas a conjuntos
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    resultado = {
        "interseccion": conjunto1 & conjunto2,          # elementos comunes
        "union": conjunto1 | conjunto2,                 # todos sin duplicados
        "diferencia_simetrica": conjunto1 ^ conjunto2   # en uno u otro, pero no en los dos
    }
    return resultado


# Prueba
a = [1, 2, 3, 4, 5, 5]
b = [4, 5, 6, 7, 7]

print("Lista 1:", a)
print("Lista 2:", b)

res = operaciones_conjuntos(a, b)
print("Interseccion:", res["interseccion"])
print("Union:", res["union"])
print("Diferencia simetrica:", res["diferencia_simetrica"])
