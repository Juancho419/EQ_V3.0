
import ctypes.wintypes
import os
import json


ruta_parametros = os.path.join(os.path.dirname(__file__), "parametros_produccion.json")
# Verificar si el archivo de parámetros existe

# Cargar parámetos del archivo JSON
try:
    with open(ruta_parametros, "r") as f:
        parametros = json.load(f)
    print("Parámetros cargados correctamente.")
except Exception as e:
    print("Error al cargar el archivo de parámetros:", e)
    exit(1)
    

def get_escritorio_path():
    CSIDL_DESKTOP = 0
    SHGFP_TYPE_CURRENT = 0
    buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
    ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_DESKTOP, None, SHGFP_TYPE_CURRENT, buf)
    return buf.value

# Prueba: mostrar ruta de escritorio en pantalla
print("Ruta del escritorio detectada:")
print(get_escritorio_path())

from datetime import datetime
import os

escritorio = get_escritorio_path()
fecha = datetime.now().strftime("%Y%m%d")
nombre_archivo = f"EQUALIZADOR_3D_GANTT_{fecha}.xlsx"
ruta_archivo = os.path.join(escritorio, nombre_archivo)

print("El archivo se guardará en:")
print(ruta_archivo)

import numpy as np
import pandas as pd

import tkinter as tk
from tkinter import messagebox

def obtener_parametros_desde_gui():
    def analizar():
        try:
            nombre = nombre_entry.get().strip()
            episodios = int(episodios_entry.get())
            duracion = int(duracion_entry.get())
            reuso = float(reuso_entry.get())  # porcentaje (ej: 25.5)
            props = int(props_entry.get())
            personajes = int(personajes_entry.get())
            environments = int(env_entry.get())
            usd_dia_text = usd_dia_entry.get().strip()
            if usd_dia_text == "":
                messagebox.showerror("Error", "El valor en USD por día no puede estar vacío.")
                return
            try:
                usd_dia = float(usd_dia_text)
            except ValueError:
                messagebox.showerror("Error", "El valor en USD por día debe ser un número válido, (Ej: 15 ó 22.5).")
                return

            # Guardar en variables globales
            global nombre_proyecto, episodios_proyecto, duracion_proyecto
            global porcentaje_reuso, props_proyecto, personajes_proyecto, environments_proyecto, usd_dia_proyecto
            nombre_proyecto = nombre
            episodios_proyecto = episodios
            duracion_proyecto = duracion
            porcentaje_reuso = reuso
            props_proyecto = props
            personajes_proyecto = personajes
            environments_proyecto = environments
            usd_dia_proyecto = usd_dia
            root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Datos inválidos. Detalle técnico: {e}")

    root = tk.Tk()
    root.title("EQUALIZADOR 3D | Parámetros del Proyecto")

    row = 0
    tk.Label(root, text="Nombre del Proyecto:").grid(row=row, column=0, padx=5, pady=5, sticky="w")
    nombre_entry = tk.Entry(root, width=25)
    nombre_entry.grid(row=row, column=1, padx=5, pady=5)
    row += 1

    tk.Label(root, text="Cantidad de episodios:").grid(row=row, column=0, padx=5, pady=5, sticky="w")
    episodios_entry = tk.Entry(root, width=10)
    episodios_entry.grid(row=row, column=1, padx=5, pady=5)
    row += 1

    tk.Label(root, text="Duración por episodio (seg):").grid(row=row, column=0, padx=5, pady=5, sticky="w")
    duracion_entry = tk.Entry(root, width=10)
    duracion_entry.grid(row=row, column=1, padx=5, pady=5)
    row += 1

    tk.Label(root, text="Porcentaje de reúso de assets (%):").grid(row=row, column=0, padx=5, pady=5, sticky="w")
    reuso_entry = tk.Entry(root, width=10)
    reuso_entry.grid(row=row, column=1, padx=5, pady=5)
    row += 1

    tk.Label(root, text="Cantidad de nuevos props :").grid(row=row, column=0, padx=5, pady=5, sticky="w")
    props_entry = tk.Entry(root, width=10)
    props_entry.grid(row=row, column=1, padx=5, pady=5)
    row += 1

    tk.Label(root, text="Cantidad de nuevos personajes :").grid(row=row, column=0, padx=5, pady=5, sticky="w")
    personajes_entry = tk.Entry(root, width=10)
    personajes_entry.grid(row=row, column=1, padx=5, pady=5)
    row += 1

    tk.Label(root, text="Cantidad de nuevos fondos/escenarios:").grid(row=row, column=0, padx=5, pady=5, sticky="w")
    env_entry = tk.Entry(root, width=10)
    env_entry.grid(row=row, column=1, padx=5, pady=5)
    row += 1
    
    tk.Label(root, text="Valor en USD por día por artista:").grid(row=row, column=0, padx=5, pady=5, sticky="w")
    usd_dia_entry = tk.Entry(root, width=10)
    usd_dia_entry.grid(row=row, column=1, padx=5, pady=5)
    row += 1

    analizar_btn = tk.Button(root, text="Analizar", command=analizar)
    analizar_btn.grid(row=row, column=0, columnspan=2, pady=12)

            
    root.mainloop()

obtener_parametros_desde_gui()

print("Nombre del proyecto:", nombre_proyecto)
print("Episodios:", episodios_proyecto)
print("Duración por episodio (seg):", duracion_proyecto)
print("Porcentaje de reúso:", porcentaje_reuso)
print("Props:", props_proyecto)
print("Personajes:", personajes_proyecto)
print("Fondos:", environments_proyecto)
print("USD/día por artista:", usd_dia_proyecto)


from calculos import calcular_tiempos_costos_arte
# calculos.py


    
resultados_arte = calcular_tiempos_costos_arte(
    props_proyecto, 
    personajes_proyecto, 
    environments_proyecto,
    parametros,
    usd_dia_proyecto
)

# Mostrar resultados
    
print("\nResumen área de arte:")
print(f"Props a desarrollar: {resultados_arte['props']}")
print(f"Personajes a desarrollar: {resultados_arte['personajes']}")
print(f"Fondos a desarrollar: {resultados_arte['environments']}")
print(f"Porcentaje de reúso declarado: {porcentaje_reuso}%")
print(f"Tiempo total estimado de arte: {resultados_arte['dias_totales_arte']:.2f} días")
print(f"Costo total de arte: {resultados_arte['costo_total_arte']:.2f} USD")

