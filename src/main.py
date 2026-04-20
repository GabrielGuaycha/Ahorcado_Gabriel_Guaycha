from Ahorcado import ESTADOS_AHORCADO
import random
import os 
import random
import os

# CAPA DE DATOS: Lectura de biblioteca externa [Pensamiento Innovador]
def obtener_palabras():
    """Lee las palabras desde un archivo de texto externo."""
    ruta_archivo = os.path.join("src", "palabras.txt")
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            # Quitamos espacios y saltos de línea de cada palabra
            palabras = [linea.strip().upper() for linea in archivo if linea.strip()]
        return palabras
    except FileNotFoundError:
        # Plan de contingencia si el archivo no existe
        return ["UIDE", "IA", "PROGRAMACION"]

# CAPA DE LÓGICA: Procesamiento modular (Caso de Uso: Validar Letra)
def validar_letra(letra, palabra_secreta, progreso):
    """Implementa la lógica de comparación y actualización de estado."""
    acierto = False
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            progreso[i] = letra
            acierto = True
    return acierto

def jugar():
    # Inicialización basada en el análisis previo
    diccionario = obtener_palabras()
    palabra_secreta = random.choice(diccionario)
    progreso = ["_"] * len(palabra_secreta)
    vidas = 6 
    letras_probadas = []

    print("--- PROYECTO AHORCADO: INGENIERÍA EN IA (UIDE) ---")

    # ESTRUCTURA REPETITIVA: Bucle de control de estado
    while vidas > 0 and "_" in progreso:
        print(f"\nPalabra: {' '.join(progreso)} | Vidas: {vidas}")

        # Calculamos el índice: (Total de vidas iniciales - vidas actuales)
        indice_dibujo = 6 - vidas
        print(ESTADOS_AHORCADO[indice_dibujo])

        # ESTRUCTURA DE SELECCIÓN: Validación de entrada
        letra = input("Ingrese una letra: ").upper()

        if len(letra) != 1 or not letra.isalpha():
            print("ERROR: Ingrese solo una letra válida.")
            continue

        if letra in letras_probadas:
            print(f"Ya probaste la '{letra}'.")
            continue

        letras_probadas.append(letra)

        # Vinculación con el diagrama de casos de uso
        if validar_letra(letra, palabra_secreta, progreso):
            print(f"¡Acierto!")
        else:
            vidas -= 1
            print(f"Letra incorrecta.")
            
    # Conclusión lógica del sistema
    if "_" not in progreso:
        print(f"\n¡VICTORIA! Has descifrado: {palabra_secreta}")
    else:
        print(f"\nDERROTA. La palabra era: {palabra_secreta}")

if __name__ == "__main__":
    jugar()