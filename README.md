# Simulador de Flujo de Recursos: Nodos Críticos de Maracaibo

Este repositorio contiene el desarrollo de un **Simulador de Flujo Vehicular** basado en modelos estocásticos y sistemas de eventos discretos. El proyecto forma parte de la cátedra de **Simulación de Sistemas (PP2)** de la **Universidad del Zulia (LUZ)**.

---

## 📋 Descripción del Proyecto
El objetivo principal es realizar el diagnóstico, modelado y optimización de la infraestructura vial urbana de Maracaibo. El enfoque es **Top-Down**: empezamos con la recolección de datos reales para construir un simulador numérico que permita identificar la configuración de semáforos que maximiza la eficiencia del flujo en nodos críticos.

## 🎯 Objetivo del Semestre: Optimización del "Sweet Time"
En esta etapa inicial, el proyecto se centra en la **Métrica Juez: Flujo Total por Ciclo ($\Phi$)**. Se busca determinar el Tiempo de Verde ($g$) óptimo para maximizar el número de vehículos que evacúan un nodo antes de llegar a la saturación o al desperdicio de tiempo operativo.

## 🧮 Fundamentos del Modelo
El simulador debe basarse en la dinámica real de despacho de colas. La lógica fundamental para calcular el flujo esperado es:

$$\Phi = 1 + \left\lfloor \frac{g - T_1}{T_{sat}} \right\rfloor$$

Donde:
*   **$g$**: Tiempo de luz verde (Variable de control).
*   **$T_1$**: Tiempo de despacho del primer vehículo (Inercia del sistema/Reacción).
*   **$T_{sat}$**: Tiempo promedio entre vehículos subsiguientes (Flujo saturado).

---

## 🚀 Hitos del Estudiante

### 1. Recolección de Datos (Diagnóstico del Paciente)
Cada equipo de trabajo debe realizar mediciones de campo en el nodo asignado para obtener valores estadísticamente significativos de $T_1$ y $T_{sat}$.

### 2. Construcción del Simulador Numérico
Desarrollar un script en **Python** (compatible con Google Colab) que modele el nodo. El script debe:
*   Iterar sobre un rango de tiempos de verde (ej. de 10s a 90s).
*   Calcular el flujo total $\Phi$ para cada intervalo.
*   Generar una gráfica de **Eficiencia de Flujo ($\Phi$ vs $g$)**.

### 3. Identificación del "Sweet Time"
Analizar los resultados para encontrar el punto donde el incremento del tiempo de verde deja de producir un aumento proporcional en el flujo (punto de inflexión o saturación).

### 4. Cuadro Comparativo Final
Presentar un diagnóstico que compare:
*   **Estado Actual:** Flujo medido con la configuración actual del semáforo.
*   **Estado Optimizado:** Flujo máximo teórico y el tiempo de verde recomendado.

---

## 📂 Estructura del Repositorio
```text
├── data/                  # Archivos CSV/Excel con mediciones de campo.
├── docs/                  # Diagramas de flujo y documentación técnica.
├── simulations/           # Scripts de Python con el motor del simulador.
└── workspace/             # Carpetas independientes por nodo/estudiante.



🛠️ Requisitos Tecnológicos

    Lenguaje: Python 3.x

    Entorno: Google Colab

    Librerías: Matplotlib (Visualización), NumPy (Cálculos), Pandas (Data).

    Modelado: Graphviz para representación de grafos de flujo.

Facultad de Ingeniería - Universidad del Zulia (LUZ)

Maracaibo, Venezuela.


### Tips para que quede perfecto:
1.  **Borra todo** lo que está en la línea 1 del editor de GitHub antes de pegar.
2.  Dale al botón **"Preview"** (arriba a la izquierda en tu captura) antes de guardar para confirmar que se vea bien.
3.  Si usas el celular para pegar, a veces el portapapeles elimina los saltos de línea; intenta "seleccionar todo" este bloque de código gris aquí arriba.

¡Con eso el repo de PP2 quedará impecable para los muchachos!
