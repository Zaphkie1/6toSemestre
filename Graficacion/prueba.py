import matplotlib.pyplot as plt

# Programa de traslacion
# Elaborado por Edgar Israel Trejo Vazquez y Denisse Delgadillo Pinedo
# Nota: Para usar este programa es necesario tener instalado Python y la librebria matplotlib

# Definir los objetos disponibles para dibujar
objetos = {
    "cuadrado": [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)],
    "triangulo": [(0, 0), (1, 0), (0.5, 1), (0, 0)],
    "rectangulo": [(0, 0), (2, 0), (2, 1), (0, 1), (0, 0)],
    "pentagono": [(0, 0), (1, 0), (1.5, 0.5), (1, 1), (0, 1), (0, 0)],
    "romboide": [(0, 0), (2.5, 0), (3, 1), (.8, 1),(0,0)]
}


# Función para dibujar un objeto en las coordenadas especificadas
def dibujar_objeto(objeto, color='b'):
    x = [p[0] for p in objeto]
    y = [p[1] for p in objeto]
    plt.plot(x, y, color=color)

# Función para trasladar y escalar un objeto en las coordenadas especificadas
def trasladar_y_escalar_objeto(objeto, dx, dy, escala):
    nuevo_objeto = [(p[0] * escala + dx, p[1] * escala + dy) for p in objeto]
    return nuevo_objeto

# Pedir al usuario la cantidad de figuras a generar
num_figuras = int(input("Ingrese la cantidad de figuras que desea generar: "))

# Pedir al usuario las coordenadas, nombres y escalas de los objetos
coordenadas_objetos = []
nombres_objetos = []
escalas_objetos = []
for i in range(num_figuras):
    x = float(input(f"Ingrese la coordenada x del objeto {i+1}: "))
    y = float(input(f"Ingrese la coordenada y del objeto {i+1}: "))
    coordenadas_objetos.append((x, y))
    nombre_objeto = input(f"Ingrese el nombre del objeto {i+1} (entre cuadrado, triangulo, rectangulo, pentagono o romboide): ")
    nombres_objetos.append(nombre_objeto)
    escala_objeto = float(input(f"Ingrese el factor de escala para el objeto {i+1}: "))
    escalas_objetos.append(escala_objeto)

# Pedir al usuario las distancias de traslación
dx = float(input("Ingrese la distancia dx para la traslación: "))
dy = float(input("Ingrese la distancia dy para la traslación: "))

# Establecer el tamaño de la pantalla
plt.figure(figsize=(10, 10))

# Dibujar los objetos originales
for i, coordenada in enumerate(coordenadas_objetos):
    objeto = objetos.get(nombres_objetos[i].lower(), [])
    if objeto:
        objeto_trasladado = trasladar_y_escalar_objeto(objeto, coordenada[0], coordenada[1], escalas_objetos[i])
        dibujar_objeto(objeto_trasladado, color='blue')

# Dibujar los objetos trasladados
for i, coordenada in enumerate(coordenadas_objetos):
    objeto = objetos.get(nombres_objetos[i].lower(), [])
    if objeto:
        objeto_trasladado = trasladar_y_escalar_objeto(objeto, coordenada[0] + dx, coordenada[1] + dy, escalas_objetos[i])
        dibujar_objeto(objeto_trasladado, color='red')
        plt.text(coordenada[0] + dx, coordenada[1] + dy, f"({dx}, {dy})", fontsize=10, ha='center', va='center')

        # Dibujar una línea entre los puntos originales y trasladados
        x_values = [coordenada[0], coordenada[0] + dx]
        y_values = [coordenada[1], coordenada[1] + dy]
        plt.plot(x_values, y_values, linestyle='--', color='black')

# Agregar leyenda
plt.plot([0], [0], color='blue', label='Objetos originales')
plt.plot([0], [0], color='red', label='Objetos trasladados')
plt.legend(loc='upper right')

# Configuración del gráfico
plt.axis([0, 1366, 768, 0])  # Establecer los límites de los ejes
plt.xlabel('1366')
plt.ylabel('768')
plt.title('Objetos trasladados')
plt.grid(True)

# Mostrar el gráfico
plt.show()
