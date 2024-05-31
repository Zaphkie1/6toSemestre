import matplotlib.pyplot as plt

# Programa de Reflexion
# Elaborado por Edgar Israel Trejo Vazquez y Denisse Delgadillo Pinedo
# Nota: Para usar este programa es necesario tener instalado Python y la librebria matplotlib


# Definir los objetos disponibles para dibujar
objetos = {
    "cuadrado": [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)],
    "triangulo": [(0, 0), (1, 0), (0.5, 1), (0, 0)],
    "rectangulo": [(0, 0), (2, 0), (2, 1), (0, 1), (0, 0)],
    "pentagono": [(0, 0), (1, 0), (1.5, 0.5), (1, 1), (0, 1), (0, 0)],
    "romboide": [(0, 0), (2.5, 0), (3, 1), (0.8, 1), (0, 0)]
}

# Factor de escala
factor_escala = 30

# Función para escalar los puntos del objeto
def escalar_objeto(objeto, factor):
    return [(p[0] * factor, p[1] * factor) for p in objeto]

# Función para reflejar los puntos del objeto
def reflejar_objeto(objeto, direccion):
    if direccion == 'a':
        return [(p[0], -p[1]) for p in objeto]
    elif direccion == 'b':
        punto_referencia = max(objeto, key=lambda p: p[1])
        return [(p[0], 2 * punto_referencia[1] - p[1]) for p in objeto]
    elif direccion == 'i':
        return [(-p[0], p[1]) for p in objeto]
    elif direccion == 'd':
        punto_referencia = max(objeto, key=lambda p: p[0])
        return [(2 * punto_referencia[0] - p[0], p[1]) for p in objeto]
    else:  # incluye 'n' para ninguna reflexión
        return objeto

# Función para dibujar un objeto en las coordenadas especificadas
def dibujar_objeto(objeto, traslacion, color='b', estilo='-'):
    x = [p[0] + traslacion[0] for p in objeto]
    y = [p[1] + traslacion[1] for p in objeto]
    plt.plot(x, y, color=color, linestyle=estilo)

# Coordenadas y escalas predefinidas para los objetos
coordenadas_objetos = [(100, 100), (300, 100), (500, 100), (700, 100), (900, 100)]
nombres_objetos = ["cuadrado", "triangulo", "rectangulo", "pentagono", "romboide"]

# Solicitar al usuario la dirección de la reflexión para cada objeto
direcciones_reflexion = []
for nombre in nombres_objetos:
    direccion = input(f"Ingrese la dirección de reflexión para {nombre} (a: arriba, b: abajo, i: izquierda, d: derecha, n: ninguna): ").strip().lower()
    direcciones_reflexion.append(direccion)

# Establecer el tamaño de la pantalla
plt.figure(figsize=(10, 10))

# Dibujar los objetos
for i, coordenada in enumerate(coordenadas_objetos):
    objeto = objetos.get(nombres_objetos[i].lower(), [])
    if objeto:
        objeto_escalado = escalar_objeto(objeto, factor_escala)
        
        # Dibujar el objeto original
        dibujar_objeto(objeto_escalado, coordenada, color='blue', estilo='-')
        
        # Verificar la dirección de reflexión
        direccion_reflexion = direcciones_reflexion[i]
        if direccion_reflexion != 'n':  # Si la dirección no es "ninguna"
            # Dibujar el objeto reflejado
            objeto_reflejado = reflejar_objeto(objeto_escalado, direccion_reflexion)
            dibujar_objeto(objeto_reflejado, coordenada, color='red', estilo='-')


# Agregar leyenda
plt.plot([0], [0], color='blue', label='Original')
plt.plot([0], [0], color='red', label='Reflejado')
plt.legend(loc='upper right')

# Configuración del gráfico
plt.axis([0, 1366, 768, 0])  # Establecer los límites de los ejes
plt.xlabel('Ancho')
plt.ylabel('Alto')
plt.title('Objetos trasladados, escalados y reflejados')
plt.grid(True)

# Mostrar el gráfico
plt.show()
