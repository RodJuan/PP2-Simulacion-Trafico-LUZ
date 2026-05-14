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
*   **$g$ (Verde):** Tiempo total de luz verde + amarilla asignado al canal (Variable de control).
*   **$T_1$ (Inercia):** Tiempo que tarda el primer vehículo en arrancar y cruzar la linea de pare (Reacción).
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
Subir a su respectiva carpeta:
*   `diagrama_nodo.png`: Mapa técnico numerado.
*   `datos_campo.csv`: Dataset con las mediciones detalladas. Incluir hora y fecha de inicio de medicion.
*   `observaciones.md`: Notas sobre el estado de la vía.

### 🤖 Uso de Inteligencia Artificial:
Se recomienda y alienta el uso de **IA Generativa (ChatGPT, Claude, Grok, Gemini)** para:
*   Construir la estructura del **Simulador Numérico** en Python.
*   Optimizar el procesamiento del archivo `.csv`.
*   Generar gráficas comparativas entre el Escenario A y el Escenario B.

---

### 🕒 Nota Técnica sobre el Tiempo de Saturación ($T_{sat}$)

Para que el simulador sea preciso, la medición del **$T_{sat}$** debe hacerse bajo el concepto de **"Línea de Pare"**. No deben medir cuánto tarda un vehículo en cruzar toda la calle, sino el intervalo entre vehículos al pasar por un punto fijo.

#### ¿Cómo medirlo en campo?
Sigan esta secuencia por cada carril:

1. **Arranque ($T_1$):** Inicien el cronómetro al cambiar la luz a **Verde**. Detengan (o marquen "lap") justo cuando la defensa delantera del **primer vehículo** pise la línea de pare.
2. **Saturación ($T_{sat}$):** Sin detener el cronómetro, marquen un "lap" cada vez que la defensa delantera del **vehículo siguiente** pise la misma línea de pare.
    * **Intervalo 1:** Entre Carro 1 y Carro 2.
    * **Intervalo 2:** Entre Carro 2 y Carro 3.
    * **Intervalo 3:** Entre Carro 3 y Carro 4.
3. **Promedio:** El $T_{sat}$ final será el promedio de esos intervalos (Laps) registrados *después* del primer vehículo.

> **⚠️ IMPORTANTE:** Solo midan el $T_{sat}$ de los vehículos que forman parte de la **cola acumulada** durante el rojo. Si un vehículo llega a la intersección sin detenerse porque el semáforo ya estaba en verde, ese tiempo **no es válido** para el cálculo de saturación, ya que no representa la presión de salida del nodo.

#### 📝 Ejemplo de Registro de Datos
Si en un ciclo miden:

* **Verde inicia:** 0.0s
* **Carro 1 cruza:** 3.8s → ($T_1 = 3.8s$)
* **Carro 2 cruza:** 5.9s (Intervalo: 2.1s)
* **Carro 3 cruza:** 8.1s (Intervalo: 2.2s)
* **Carro 4 cruza:** 10.1s (Intervalo: 2.0s)

**$T_{sat}$ de este ciclo:** $(2.1 + 2.2 + 2.0) / 3 = \mathbf{2.1s}$

## 🧠 Interpretación de Ingeniería
*   **Si $\Phi_{B} >> \Phi_{A}$:** Se justifica proponer la eliminación de giros a la izquierda.
*   **Si $\Phi_{B} \approx \Phi_{A}$:** La congestión es estructural y requiere cambios en la infraestructura física.

---
**Facultad Experimental de Ciencias (FEC) - Universidad del Zulia (LUZ)**
*Maracaibo, Venezuela.*
