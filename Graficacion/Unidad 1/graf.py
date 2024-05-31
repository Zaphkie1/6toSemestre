import numpy as np
import matplotlib.pyplot as plt

# Definir función para rotar un punto alrededor de un punto central
def rotate_point(px, py, cx, cy, angle):
    angle_rad = np.radians(angle)
    cos_angle = np.cos(angle_rad)
    sin_angle = np.sin(angle_rad)
    translated_x = px - cx
    translated_y = py - cy
    rotated_x = translated_x * cos_angle - translated_y * sin_angle
    rotated_y = translated_x * sin_angle + translated_y * cos_angle
    return rotated_x + cx, rotated_y + cy

# Datos de las líneas originales
#line1 = [(100,200), (400, 500)]
line2 = [(10,10), (700, 700)]

# Puntos centrales
#center1 = ((line1[0][0] + line1[1][0]) / 2, (line1[0][1] + line1[1][1]) / 2)
center2 = ((line2[0][0] + line2[1][0]) / 2, (line2[0][1] + line2[1][1]) / 2)

# Ángulos de rotación
angles = [30, 60, 140, -70, -110]

# Crear un gráfico
fig, ax = plt.subplots()
fig.set_size_inches(10, 6)  # Ajustar el tamaño del gráfico (ancho, alto)
ax.set_aspect('equal', 'box')

# Establecer límites fijos para los ejes
ax.set_xlim(-100, 1000)
ax.set_ylim(-100, 1000)

# Dibujar líneas originales
#ax.plot([line1[0][0], line1[1][0]], [line1[0][1], line1[1][1]], label='Línea 1 Original', color='blue')
ax.plot([line2[0][0], line2[1][0]], [line2[0][1], line2[1][1]], label='Línea 2 Original', color='green')

# Dibujar líneas rotadas
colors = ['red', 'orange', 'purple', 'cyan', 'magenta']
for angle, color in zip(angles, colors):
    # Rotar Línea 1
#    r1p1 = rotate_point(line1[0][0], line1[0][1], center1[0], center1[1], angle)
#    r1p2 = rotate_point(line1[1][0], line1[1][1], center1[0], center1[1], angle)
#    ax.plot([r1p1[0], r1p2[0]], [r1p1[1], r1p2[1]], label=f'Línea 1 Rotada {angle}°', color=color, linestyle='--')

    # Rotar Línea 2
    r2p1 = rotate_point(line2[0][0], line2[0][1], center2[0], center2[1], angle)
    r2p2 = rotate_point(line2[1][0], line2[1][1], center2[0], center2[1], angle)
    ax.plot([r2p1[0], r2p2[0]], [r2p1[1], r2p2[1]], label=f'Línea 2 Rotada {angle}°', color=color, linestyle='-.')

# Añadir leyenda y mostrar gráfico
ax.legend()
# Configuración del gráfico
plt.axis([0, 1366, 768, 0])  # Establecer los límites de los ejes
plt.xlabel('1366')
plt.ylabel('768')
plt.title('Objetos trasladados')
plt.grid(True)

# Mostrar el gráfico
plt.show()

