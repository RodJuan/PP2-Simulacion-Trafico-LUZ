# 🚦 Simulador de Flujo de Recursos: Nodos Críticos de Maracaibo

Este repositorio contiene el desarrollo de un **Simulador de Flujo Vehicular** para la cátedra de **Simulación de Sistemas (PP2)** de la **Facultad Experimental de Ciencias (FEC)** en la Universidad del Zulia (LUZ).

---

## 📋 Descripción del Proyecto
El proyecto consiste en un **Análisis de Reingeniería de Fases**. Buscamos determinar si un cambio en la lógica de activación de semáforos puede optimizar el flujo total ($\Phi$) sin alterar la infraestructura física del nodo Cuartel Libertador - FEC.

## 🎯 Objetivo: Comparativa de Escenarios
1.  **Escenario A (Actual):** Activación secuencial (Fase 1 → 2 → 3 → 4). Solo un flujo se mueve a la vez.
2.  **Escenario B (Propuesto):** Activación simultánea opuesta (Fase Alfa: 1+3 / Fase Beta: 2+4). Maximiza el flujo directo eliminando giros a la izquierda.

---

## 🧮 Fundamento Matemático (Modelo de Despacho)

Para predecir el comportamiento del nodo, utilizaremos la fórmula de despacho de colas:

$$\Phi = 1 + \left\lfloor \frac{g - T_1}{T_{sat}} \right\rfloor$$

### 🔍 Glosario de Términos:
*   **$\Phi$ (Flujo):** Número total de vehículos que logran cruzar la línea de pare en un tiempo de verde.
*   **$g$ (Verde):** Tiempo total de luz verde asignado al canal (Variable de control).
*   **$T_1$ (Inercia):** Tiempo que tarda el primer vehículo en arrancar y cruzar (Reacción).
*   **$T_{sat}$ (Saturación):** Tiempo promedio entre los vehículos que vienen detrás del primero.

### 💡 Ejemplo Numérico:
Si en el canal 1.1 tenemos un verde de **$g = 30s$**, una inercia de **$T_1 = 4.0s$** y un tiempo entre vehículos de **$T_{sat} = 2.2s$**:
1.  Restamos la inercia del verde: $30 - 4 = 26s$ (Tiempo disponible para el resto de la cola).
2.  Dividimos entre la saturación: $26 / 2.2 = 11.81$.
3.  Aplicamos la función piso ($\lfloor \rfloor$): $11$ vehículos.
4.  Sumamos el primer vehículo: $11 + 1 = 12$ vehículos.
**Resultado:** $\Phi = 12$ vehículos por ciclo.

---

## 📊 Fase 1: Levantamiento de Datos (Tarea de Campo)
Cada equipo debe generar el archivo **`datos_campo.csv`** con las siguientes mediciones (mínimo 5 ciclos en hora pico):

1.  **Parámetros de la Ecuación:** Medir $T_1$ y $T_{sat}$ por cada canal.
2.  **Validación Manual ($\Phi_{obs}$):** Contar físicamente cuántos autos pasan en cada verde y comparar con la fórmula usando:
    $$\Phi_{manual} = \frac{N_{total\_vehiculos}}{t_{verde}}$$
3.  **Matriz de Giro (%):** Porcentaje de autos que van recto, izquierda o derecha por canal.

---

## 🚀 Entregables y Desarrollo
Subir a la carpeta `workspace/`:
*   `diagrama_nodo.png`: Mapa técnico numerado.
*   `datos_campo.csv`: Dataset con las mediciones detalladas. Incluir hora y fecha de inicio de medicion.
*   `observaciones.md`: Notas sobre el estado de la vía.

### 🤖 Uso de Inteligencia Artificial:
Se recomienda y alienta el uso de **IA Generativa (ChatGPT, Claude, Grok, Gemini)** para:
*   Construir la estructura del **Simulador Numérico** en Python.
*   Optimizar el procesamiento del archivo `.csv`.
*   Generar gráficas comparativas entre el Escenario A y el Escenario B.

---

## 🧠 Interpretación de Ingeniería
*   **Si $\Phi_{B} >> \Phi_{A}$:** Se justifica proponer la eliminación de giros a la izquierda.
*   **Si $\Phi_{B} \approx \Phi_{A}$:** La congestión es estructural y requiere cambios en la infraestructura física.

---
**Facultad Experimental de Ciencias (FEC) - Universidad del Zulia (LUZ)**
*Maracaibo, Venezuela.*
