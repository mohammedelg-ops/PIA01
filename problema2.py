# Problema 2. Frecuencia de palabras en un texto
import os
import string


def frecuencia_palabras(palabras, ruta):
    # Leer el fichero y pasarlo a minusculas
    with open(ruta, "r", encoding="utf-8") as fichero:
        texto = fichero.read().lower()

    # Quitar los signos de puntuacion (tambien ¿ y ¡)
    for signo in string.punctuation + "¿¡":
        texto = texto.replace(signo, " ")

    lista_texto = texto.split()

    # Diccionario: clave = palabra, valor = veces que aparece
    frecuencias = {}
    for palabra in palabras:
        palabra = palabra.lower()
        frecuencias[palabra] = lista_texto.count(palabra)

    # Ordenar por la palabra
    return dict(sorted(frecuencias.items()))


# Programa de prueba
# (texto.txt tiene que estar en la misma carpeta que este fichero)
carpeta = os.path.dirname(os.path.abspath(__file__))
ruta = os.path.join(carpeta, "texto.txt")

palabras_buscar = ["python", "datos", "inteligencia", "modelo", "aprendizaje", "java"]
resultado = frecuencia_palabras(palabras_buscar, ruta)

print("Frecuencia de las palabras en texto.txt:")
for palabra, veces in resultado.items():
    print(f"{palabra}: {veces}")
