# 🚦 Simulador de Flujo de Recursos: Nodos Críticos de Maracaibo

Este repositorio contiene el desarrollo de un **Simulador de Flujo Vehicular** para la cátedra de **Simulación de Sistemas (PP2)** de la **Facultad Experimental de Ciencias (FEC)** en la Universidad del Zulia (LUZ).

---

## 📋 Descripción del Proyecto
El proyecto consiste en un **Análisis de Reingeniería de Fases**. Buscamos determinar si un cambio en la lógica de activación de semáforos puede optimizar el flujo total ($\Phi$) sin alterar la infraestructura física (aceras/canales) del nodo Cuartel Libertador - FEC.

## 🎯 Objetivo: Comparativa de Escenarios de Flujo
El equipo debe modelar y comparar dos topologías de control para un ciclo de tiempo constante:

### Escenario A: Secuencial (Estado Actual)
Activación sucesiva de cada semáforo: 
**Fase 1** → **Fase 2** → **Fase 3** → **Fase 4** → (Reinicio)
* **Limitante:** Solo un flujo principal se mueve a la vez.

### Escenario B: Simultáneo Opuesto (Propuesta)
Activación de flujos paralelos no colisionantes:
1.  **Fase Alfa (1+3):** Canales lineales 1.1, 1.2 y 3.1, 3.2 activos simultáneamente.
2.  **Fase Beta (2+4):** Canales lineales 2.1, 2.2 y 4.1, 4.2 activos simultáneamente.
* **Hipótesis:** La eliminación de los giros a la izquierda (canales x.3) en favor de flujos directos masivos maximiza el $\Phi$ total por ciclo.

---

## 📊 Fase 1: Levantamiento de Datos (Tarea de Campo)
Antes de programar el simulador, cada equipo debe generar el **Dataset Maestro** de su intersección asignada.

### 1. Digitalización del Nodo (Diagrama Técnico)
Cada equipo debe entregar un diagrama detallado de su intersección (usando Paint, herramientas móviles o CAD). Debe incluir:
* Numeración de semáforos (Fases).
* Identificación de canales de cada avenida (Ej: 1.1, 1.2, 1.3).
* Sentido de las flechas de flujo.

### 2. Protocolo de Medición de Flujo
Registrar promedios de al menos 5 ciclos completos en horas pico:
* **Tiempos Base:** $g$ (verde actual) y $C$ (tiempo total del ciclo).
* **$T_1$:** Tiempo de reacción del primer vehículo al iniciar el verde.
* **$T_{sat}$:** Tiempo promedio entre vehículos en flujo saturado.
* **$\Phi$ (Flujo):** Total de autos que logran cruzar por ciclo.

### 3. Matriz de Intención de Giro (%)
Registrar el promedio de intención de maniobra por carril:
* **% Sigue Recto.**
* **% Giro a la Izquierda** (Flujo de conflicto).
* **% Giro a la Derecha** (Flujo de incorporación).

---

## 🚀 Entregables (Semana 1)
Subir a la carpeta correspondiente en `workspace/`:
1.  `diagrama_nodo.png`: Mapa técnico del nodo.
2.  `datos_campo.csv`: Tabla con promedios de $T_1$, $T_{sat}$, $\Phi$ y porcentajes de giro.
3.  `observaciones.md`: Notas sobre obstáculos externos (baches, paradas, etc.).

---

## 🧠 Interpretación de Ingeniería
* **Si $\Phi_{B} >> \Phi_{A}$:** Se recomienda prohibir el giro a la izquierda en ese nodo para optimizar la Av. Universidad.
* **Si $\Phi_{B} \approx \Phi_{A}$:** La congestión es estructural; el cambio de fases no justifica la eliminación de cruces.

---
**Facultad Experimental de Ciencias (FEC) - Universidad del Zulia (LUZ)** *Maracaibo, Venezuela.*
