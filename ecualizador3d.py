
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
            episodios = episodios_entry.get().strip()
            duracion = duracion_entry.get().strip()
            reuso = reuso_entry.get().strip()
            props = props_entry.get().strip()
            personajes = personajes_entry.get().strip()
            environments = env_entry.get().strip()
            usd_dia = usd_dia_entry.get().strip()

            # Validación de campos vacíos
            if not all([nombre, episodios, duracion, reuso, props, personajes, environments, usd_dia]):
                messagebox.showerror("Error", "All fields are required.")
                return
            
            # --- Preproducción (PRE) ---
            
            # Validación de enteros positivos (no acepta decimales ni negativos)
            for field, value in [
                ("Episodes", episodios),
                ("Duration", duracion),
                ("Re-use %", reuso),
                ("Props", props),
                ("Characters", personajes),
                ("Environments", environments)
            ]:
                if not value.isdigit() or int(value) < 0:
                    messagebox.showerror("Error", f"{field} must be a non-negative integer (no decimals).")
                    return

            # Validación de USD/día (puede ser decimal, pero no negativo)
            try:
                usd_dia_float = float(usd_dia)
                if usd_dia_float < 0:
                    messagebox.showerror("Error", "USD per day must be a non-negative number.")
                    return
            except ValueError:
                messagebox.showerror("Error", "USD per day must be a number (e.g. 10 or 20.5).")
                return
            
            # --- PRODUCCIÓN (PROD) ---
            

            # Validación de artistas de animatic
            animatic_artistas = animatic_artistas_entry.get().strip()
            if not animatic_artistas.isdigit() or int(animatic_artistas) < 1:
                messagebox.showerror("Error", "Animatic Artists must be an integer ≥ 1.")
                return

            # Validación de artistas de layout/animación
            layout_animacion_artistas = layout_animacion_artistas_entry.get().strip()
            if not layout_animacion_artistas.isdigit() or int(layout_animacion_artistas) < 3:
                messagebox.showerror("Error", "Layout/Animation Artists must be an integer ≥ 3.")
                return

            # Guardar globales
            global animatic_artistas_global, layout_animacion_artistas_global
            animatic_artistas_global = int(animatic_artistas)
            layout_animacion_artistas_global = int(layout_animacion_artistas)

        
            
            
        except Exception as e:
            messagebox.showerror("Error", f"Technical error: {e}")


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
    
    row += 1
    tk.Label(root, text="--- PROD ---", font=("Arial", 10, "bold")).grid(row=row, column=0, columnspan=2, pady=(15, 5))

    row += 1
    tk.Label(root, text="Number of Animatic Artists (min 1):").grid(row=row, column=0, padx=5, pady=5, sticky="w")
    animatic_artistas_entry = tk.Entry(root, width=10)
    animatic_artistas_entry.insert(0, "1")
    animatic_artistas_entry.grid(row=row, column=1, padx=5, pady=5)

    row += 1
    tk.Label(root, text="Number of Layout/Animation Artists (min 3):").grid(row=row, column=0, padx=5, pady=5, sticky="w")
    layout_animacion_artistas_entry = tk.Entry(root, width=10)
    layout_animacion_artistas_entry.insert(0, "3")
    layout_animacion_artistas_entry.grid(row=row, column=1, padx=5, pady=5)

    #Botón de analizar

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

# --- PRODUCCIÓN (PROD) ---

from calculos import calcular_tiempos_costos_prod

resultado_prod = calcular_tiempos_costos_prod(
    episodios_proyecto,
    duracion_proyecto,
    animatic_artistas_global,
    layout_animacion_artistas_global,
    parametros,
    usd_dia_proyecto
)

print("\nProduction Summary (PROD):")
print(f"Animatic: {resultados_prod['dias_animatic_por_ep']:.2f} days/episode, total {resultados_prod['dias_animatic_total']:.2f} days, cost: ${resultados_prod['costo_animatic']:.2f}")
print(f"Layout: {resultados_prod['dias_layout_por_ep']:.2f} days/episode, total {resultados_prod['dias_layout_total']:.2f} days, cost: ${resultados_prod['costo_layout']:.2f}")
print(f"Animation: {resultados_prod['dias_animacion_por_ep']:.2f} days/episode, total {resultados_prod['dias_animacion_total']:.2f} days, cost: ${resultados_prod['costo_animacion']:.2f}")

# Resumen total de días y costos de producción
total_prod_days = (
    resultados_prod['dias_animatic_total'] +
    resultados_prod['dias_layout_total'] +
    resultados_prod['dias_animacion_total']
)
total_prod_cost = (
    resultados_prod['costo_animatic'] +
    resultados_prod['costo_layout'] +
    resultados_prod['costo_animacion']
)
print(f"\nTotal production days: {total_prod_days:.2f}")
print(f"Total production cost: ${total_prod_cost:.2f}")