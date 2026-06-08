
# Programa para generar el .csv listo para ser llenado con data real en campo. La data que contiene no es real, solo de muestra y deberia ser reemplazada por la real.
import csv

# Definición de las columnas del Dataset Maestro
headers = [
    "semaforo",      # Número de semáforo (1, 2, 3, 4)
    "canal",         # Identificador del canal (Ej: 1.1, 1.2, 1.3)
    "g_verde",       # Tiempo actual de luz verde en segundos
    "C_ciclo",       # Tiempo total del ciclo en segundos
    "T1_inercia",    # Tiempo de arranque del primer vehículo (promedio)
    "Tsat_saturac",  # Tiempo entre vehículos subsiguientes (promedio)
    "pct_recto",     # Porcentaje de vehículos que siguen derecho
    "pct_izq",       # Porcentaje de vehículos que giran a la izquierda
    "pct_der",       # Porcentaje de vehículos que giran a la derecha
    "phi_obs"        # Flujo observado manualmente (conteo real por verde)
]

# Datos de ejemplo basados en el Nodo Cuartel Libertador - FEC
# Los estudiantes deben reemplazar estos valores con sus mediciones reales
rows_ejemplo = [
    ["1", "1.1", "30", "120", "4.0", "2.2", "80", "0", "20", "12"],
    ["1", "1.2", "30", "120", "4.2", "2.3", "100", "0", "0", "11"],
    ["1", "1.3", "30", "120", "5.0", "3.1", "0", "100", "0", "8"],
    ["2", "2.1", "25", "120", "3.8", "2.1", "90", "0", "10", "11"],
    ["3", "3.1", "30", "120", "4.1", "2.2", "85", "0", "15", "12"],
    ["4", "4.1", "25", "120", "3.9", "2.4", "75", "25", "0", "9"]
]

nombre_archivo = "datos_campo.csv"

# Escritura del archivo CSV
with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)     # Escribe la línea de encabezados
    writer.writerows(rows_ejemplo) # Escribe las filas de ejemplo técnico

print(f"✅ Archivo '{nombre_archivo}' generado con éxito.")
print("Diles a los estudiantes que usen esta estructura y reemplacen los datos de ejemplo.")
