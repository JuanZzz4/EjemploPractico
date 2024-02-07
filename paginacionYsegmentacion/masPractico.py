class PaginadorSegmentador:
    def __init__(self, datos):
        self.datos = datos

    def paginar(self, tamano_pagina):
        paginas = []
        for i in range(0, len(self.datos), tamano_pagina):
            paginas.append(self.datos[i:i+tamano_pagina])
        return paginas

    def segmentar(self, tamano_segmento):
        segmentos = []
        for i in range(0, len(self.datos), tamano_segmento):
            segmentos.append(self.datos[i:i+tamano_segmento])
        return segmentos

    def obtener_pagina(self, numero_pagina, tamano_pagina):
        inicio = (numero_pagina - 1) * tamano_pagina
        fin = inicio + tamano_pagina
        return self.datos[inicio:fin]

    def obtener_segmento(self, numero_segmento, tamano_segmento):
        inicio = (numero_segmento - 1) * tamano_segmento
        fin = inicio + tamano_segmento
        return self.datos[inicio:fin]


# Datos de ejemplo
datos = list(range(1, 101))  # Lista del 1 al 100

paginador_segmentador = PaginadorSegmentador(datos)

# Paginación y segmentación
tamano_pagina = 10
tamano_segmento = 5

paginas = paginador_segmentador.paginar(tamano_pagina)
segmentos = paginador_segmentador.segmentar(tamano_segmento)

# Mostrar resultados
print("Paginación:")
for i, pagina in enumerate(paginas, 1):
    print(f"Página {i}: {pagina}")

print("\nSegmentación:")
for i, segmento in enumerate(segmentos, 1):
    print(f"Segmento {i}: {segmento}")

# Ejemplos de obtener una página y un segmento específico
numero_pagina = 3
numero_segmento = 2

pagina_seleccionada = paginador_segmentador.obtener_pagina(numero_pagina, tamano_pagina)
segmento_seleccionado = paginador_segmentador.obtener_segmento(numero_segmento, tamano_segmento)

print(f"\nContenido de la página {numero_pagina}: {pagina_seleccionada}")
print(f"Contenido del segmento {numero_segmento}: {segmento_seleccionado}")
