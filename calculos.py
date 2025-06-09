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
 
def calcular_tiempos_costos_prod(
    num_episodios,
    duracion_ep,
    animatic_artistas,
    layout_animacion_artistas,
    parametros,
    usd_dia
):
    cuotas = parametros["cuotas"]  # {'animatic': 26, 'layout': 30, 'animacion': 16.8, ...}

    # Animatic
    dias_animatic_por_ep = duracion_ep / (cuotas["animatic"] * animatic_artistas)
    dias_animatic_total = dias_animatic_por_ep * num_episodios
    costo_animatic = dias_animatic_total * animatic_artistas * usd_dia

    # Layout
    dias_layout_por_ep = duracion_ep / (cuotas["layout"] * layout_animacion_artistas)
    dias_layout_total = dias_layout_por_ep * num_episodios
    costo_layout = dias_layout_total * layout_animacion_artistas * usd_dia

    # Animación
    dias_animacion_por_ep = duracion_ep / (cuotas["animacion"] * layout_animacion_artistas)
    dias_animacion_total = dias_animacion_por_ep * num_episodios
    costo_animacion = dias_animacion_total * layout_animacion_artistas * usd_dia

    return {
        "dias_animatic_por_ep": dias_animatic_por_ep,
        "dias_layout_por_ep": dias_layout_por_ep,
        "dias_animacion_por_ep": dias_animacion_por_ep,
        "dias_animatic_total": dias_animatic_total,
        "dias_layout_total": dias_layout_total,
        "dias_animacion_total": dias_animacion_total,
        "costo_animatic": costo_animatic,
        "costo_layout": costo_layout,
        "costo_animacion": costo_animacion
    }
   
