# PP2-Simulacion-Trafico-LUZ

# Simulador de Flujo de Recursos - Nodos Críticos Maracaibo (PP2-LUZ)

## 📋 Descripción del Proyecto
Este proyecto busca modelar y diagnosticar el flujo vehicular en nodos críticos de la ciudad de Maracaibo (Av. Universidad) utilizando un enfoque estocástico y herramientas de software libre. El objetivo final es la reducción de la entropía del sistema mediante gestión inteligente.

## 🎯 Objetivo Semestre 1: Diagnóstico y Optimización de Ciclo
Determinar el **Tiempo de Verde Óptimo ($g_1$)** que maximiza el **Flujo Total por Ciclo ($\phi$)** en dos nodos adyacentes:
1. **Nodo 1:** Cuartel Libertador / FEC (Responsable: Carlos).
2. **Nodo 2:** IPSFA (Responsable: César).

## 🧮 Métrica Juez
La eficiencia del nodo se evaluará mediante el Flujo por Ciclo ($\phi$):
$$\phi = \sum_{i=1}^{n} V_i$$
Donde $V_i$ representa el número de vehículos que logran cruzar la línea de pare durante una fase verde completa.

## 🚀 Hoja de Ruta (Escalabilidad)
* **Fase 1 (Actual):** Modelo numérico básico y recolección de data real. Curvas $\phi = f(g_1)$.
* **Fase 2:** Interconexión de nodos (Onda Verde).
* **Fase 3:** Agentes inteligentes (Lógica Difusa) para control dinámico.

## 🛠️ Herramientas
* **Lenguaje:** Python 3.x
* **Entorno:** Google Colab (Accesibilidad total)
* **Librerías:** Pandas, Matplotlib, NumPy.
