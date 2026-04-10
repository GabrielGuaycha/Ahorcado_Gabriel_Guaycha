# Ahorcado_Gabriel_Guaycha

Este repositorio contiene el desarrollo integral del juego "El Ahorcado", disenado bajo principios de ingenieria de software para la carrera de **Ingenieria en Inteligencia Artificial** de la **UIDE**.

# Proyecto
El proyecto consiste en un sistema automatizado de adivinanza de palabras que gestiona estados criticos (incognita, acierto y error) de forma imparcial. 

**Tesis del Proyecto:** La robustez de este software no depende de su escala, sino de la coherencia entre su diseno funcional (Casos de Uso) y su implementacion logica modular, garantizando la escalabilidad y facilidad de mantenimiento.

## Estructura del Repositorio
Para cumplir con los estandares de **DevOps**, el repositorio se organiza de la siguiente manera:

`Diagrama de flujos/docs`: Contiene los diagramas de flujo y diagramas de casos de uso UML.
`/src`: Contiene el codigo fuente principal del juego (`main.py`).
`README.md`: Documentacion general.

## Especificaciones Tecnicas
[cite_start]**Lenguaje de Programacion:** Python 3.12+ [cite: 565, 743]
**Paradigma:** Programacion Estructurada y Modular.
**Librerias Utilizadas:**
    * [cite_start]`random`: Para la seleccion aleatoria de palabras desde el arreglo[cite: 571, 624].
    * `tkinter` (Opcional para graficos): Para la futura implementacion de la interfaz de ventana.


## Arquitectura de Software
El sistema esta disenado bajo un **Modelo de 3 Capas**:
1.  [cite_start]**Capa de Presentacion:** Maneja la interfaz de usuario y visualizacion de la "mascara" de la palabra. [cite: 291, 677]
2.  [cite_start]**Capa de Logica de Negocio:** Motor del juego que valida letras y gestiona el contador de vidas. [cite: 291, 681]
3.  [cite_start]**Capa de Datos:** Almacena el diccionario de palabras (Arreglos/Arrays). [cite: 291, 685]

---

## Instalacion y Uso

### Requisitos Previos
Tener instalado **Python 3** en su sistema. Se recomienda el uso de **Visual Studio Code**.

### Instalacion de Librerias (Si se usan graficos)
Si desea ejecutar la version con interfaz grafica, instale las dependencias necesarias:
```bash
pip install tk