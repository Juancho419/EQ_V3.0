# calculos.py

def calcular_tiempos_costos_arte(props, personajes, environments, parametros, usd_dia):
    # Tiempos por asset (cuotas desde el JSON)
    concept_time = parametros["cuotas"]["concept_art"]
    modelado_time = parametros["cuotas"]["modelado"]
    texturizado_time = parametros["cuotas"]["texturizado"]

    # Total días por tipo de asset
    total_concept = (props + personajes + environments) * concept_time
    total_modelado = (props + personajes + environments) * modelado_time
    total_texturizado = (props + personajes + environments) * texturizado_time

    # Suma total días arte
    dias_totales_arte = total_concept + total_modelado + total_texturizado

    # Costo total arte
    costo_total_arte = dias_totales_arte * usd_dia

    return {
        "props": props,
        "personajes": personajes,
        "environments": environments,
        "dias_totales_arte": dias_totales_arte,
        "costo_total_arte": costo_total_arte
    }
