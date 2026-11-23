# Problema 2. Frecuencia de palabras en un texto
import os
import string


def frecuencia_palabras(palabras, ruta):
    # Leer el fichero y pasar todo a minusculas
    with open(ruta, "r", encoding="utf-8") as fichero:
        texto = fichero.read().lower()

    # Quitar los signos de puntuacion (tambien los del español)
    signos = string.punctuation + "¿¡«»"
    for signo in signos:
        texto = texto.replace(signo, " ")

    lista_texto = texto.split()

    # Diccionario: clave = palabra, valor = veces que aparece
    frecuencias = {}
    for palabra in palabras:
        palabra = palabra.lower()
        frecuencias[palabra] = lista_texto.count(palabra)

    # Devolver el diccionario ordenado por la palabra
    return dict(sorted(frecuencias.items()))


# Programa de prueba
carpeta = os.path.dirname(os.path.abspath(__file__))
ruta_fichero = os.path.join(carpeta, "texto.txt")

palabras_buscar = ["python", "datos", "inteligencia", "modelo", "aprendizaje", "java"]

resultado = frecuencia_palabras(palabras_buscar, ruta_fichero)

print("Frecuencia de las palabras en", "texto.txt")
for palabra, veces in resultado.items():
    print(palabra, ":", veces)
