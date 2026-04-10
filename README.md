# Ahorcado_Gabriel_Guaycha

Este repositorio contiene el desarrollo integral del juego "El Ahorcado", disenado bajo principios de ingenieria de software para la carrera de Ingenieria en Inteligencia Artificial de la UIDE.

# Proyecto
El proyecto consiste en un sistema automatizado de adivinanza de palabras que gestiona estados criticos (incognita, acierto y error) de forma imparcial. 

**Tesis del Proyecto:** La robustez de este software no depende de su escala, sino de la coherencia entre su diseno funcional (Casos de Uso) y su implementacion logica modular, garantizando la escalabilidad y facilidad de mantenimiento.

## Estructura del Repositorio
Para cumplir con los estandares de DevOps y asegurar una organizacion profesional, el repositorio se organiza de la siguiente manera:

* `/docs`: Contiene la documentacion tecnica con los diagramas de flujo y diagramas de casos de uso UML que fundamentan la logica previa a la codificacion.
* `/src`: Carpeta raiz del codigo fuente que incluye la arquitectura modular.
* `README.md`: Documentacion general y especificaciones del sistema.

## Especificaciones Detalladas de la Implementacion

### 1. Logica del Codigo Python (main.py)
Se ha desarrollado el nucleo del programa utilizando estructuras de control de flujo avanzadas. El codigo se basa en un bucle principal `while` que evalua constantemente dos condiciones de parada: el agotamiento de recursos (vidas = 0) o la completitud de la palabra secreta. Dentro de este ciclo, se implementa validaciones mediante estructuras `if-else` para filtrar entradas no validas (numeros o caracteres especiales) y evitar la duplicidad de intentos, asegurando que la experiencia del usuario sea fluida y libre de errores logicos.

### 2. Biblioteca Visual Modular (ahorcado.py)
En lugar de saturar el archivo principal, se opto por crear `ahorcado.py`, un modulo especializado que funciona como mi libreria de "assets" visuales. Aqui se define una lista de constantes denominada `ESTADOS_AHORCADO` que utiliza arte ASCII. Cada elemento de esta lista representa una etapa visual del juego. Lo innovador es el vinculamiento dinamico: el programa principal calcula el indice de error y extrae automaticamente la imagen correspondiente, logrando una simulacion visual que evoluciona en tiempo real con cada fallo del usuario.

### 3. Gestion de Datos Externa (palabras.txt)
Para cumplir con el principio de escalabilidad, se implemento una Capa de Datos externa. El archivo `palabras.txt` funciona como una base de datos plana que contiene mas de 200 terminos tecnicos y generales. Mediante el uso de manejo de archivos de Python, el sistema lee este recurso de forma dinamica al iniciar. Esto permite que el diccionario crezca indefinidamente sin necesidad de tocar una sola linea de codigo fuente, facilitando el mantenimiento por parte de otros desarrolladores.

## Analisis de Librerias Utilizadas
Para este proyecto, se selecciono un conjunto de herramientas que garantizan la eficiencia y la independencia del sistema:

* **random:** Esta libreria es fundamental para la logica de seleccion. Util para invocar el metodo `choice`, permitiendo que el sistema elija una palabra de forma aleatoria desde la carga de datos externa, asegurando que cada partida sea una experiencia nueva.
* **os (Operating System):** Esta libreria sirve para gestionar la comunicacion con el sistema operativo del ordenador. Es vital para construir rutas de archivos relativas (path handling), asegurando que el programa encuentre el archivo `palabras.txt` sin importar en que carpeta se ejecute el proyecto.
* **ahorcado (Libreria Personalizada):** Es una biblioteca de creacion propia que actua como un repositorio de recursos graficos. Al encapsular el arte ASCII en este modulo, logro un codigo mas limpio y profesional en el archivo principal.

## Arquitectura de Software: Modelo de 3 Capas
Este documento esta diseñado en un sistema de **Modelo de 3 Capas**, un estandar en la ingenieria para separar responsabilidades:



1. **Capa de Presentacion:** Es la encargada de la interaccion directa. Aqui se gestiona el renderizado de la "mascara" (los guiones bajos de la palabra) y la proyeccion de las imagenes ASCII importadas del modulo ahorcado. Su funcion es transformar datos abstractos en una interfaz comprensible.
2. **Capa de Logica de Negocio:** Ubicada en el motor principal, es donde reside la "inteligencia" del juego. Procesa las reglas, valida si una letra pertenece a la secuencia y decide el destino del flujo (acierto o perdida de vida).
3. **Capa de Datos:** Es el cimiento del sistema. Se encarga de la persistencia y recuperacion de informacion desde el archivo de texto. Al separar los datos de la logica, garantizo que la informacion sea independiente del comportamiento del software.

---

## Instalacion y Uso

### Requisitos Previos
Es necesario tener instalado Python 3 en su sistema. Se recomienda el uso de Visual Studio Code para observar la estructura de carpetas y el resaltado de sintaxis.

### Ejecucion
Para iniciar el juego, navegue hasta la carpeta del proyecto en su terminal y ejecute:
`python src/main.py`

---

## Autor
**Gabriel Andres Guaycha Espinosa** Oficial de la Marina del Ecuador | Estudiante de Ingenieria en IA - UIDE