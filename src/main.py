import random

# CAPA DE DATOS: Persistencia local mediante arreglos
def obtener_palabras():
    """Retorna un arreglo con el diccionario de palabras secretas."""
    return ["INTELIGENCIA", "ALGORITMO", "SISTEMA", "BINARIO", "LOGICA"]

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