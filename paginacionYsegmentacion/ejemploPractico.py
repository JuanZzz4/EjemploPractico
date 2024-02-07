def paginar_datos(datos, tamano_pagina):
    paginas = []
    for i in range(0, len(datos), tamano_pagina):
        paginas.append(datos[i:i+tamano_pagina])
    return paginas

def segmentar_datos(datos, segmento):
    segmentos = []
    for i in range(0, len(datos), segmento):
        segmentos.append(datos[i:i+segmento])
    return segmentos

# Datos de ejemplo
datos = list(range(1, 101))  # Lista del 1 al 100

# Paginación
tamano_pagina = 10
paginas = paginar_datos(datos, tamano_pagina)

print("Paginación:")
for i, pagina in enumerate(paginas, 1):
    print(f"Página {i}: {pagina}")

# Segmentación
tamano_segmento = 7
segmentos = segmentar_datos(datos, tamano_segmento)

print("\nSegmentación:")
for i, segmento in enumerate(segmentos, 1):
    print(f"Segmento {i}: {segmento}")
