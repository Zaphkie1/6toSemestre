import numpy as np
import matplotlib.pyplot as plt

# Definir las coordenadas de las figuras
figuras = {
    "cuadrado": np.array([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]),
    "triangulo": np.array([(0, 0), (1, 0), (0.5, 1), (0, 0)]),
    "rectangulo": np.array([(0, 0), (2, 0), (2, 1), (0, 1), (0, 0)]),
    "pentagono": np.array([(0, 0), (1, 0), (1.5, 0.5), (1, 1), (0, 1), (0, 0)]),
    "romboide": np.array([(0, 0), (2.5, 0), (3, 1), (0.8, 1), (0, 0)])
}

# Función para rotar una figura
def rotar_figura(figura, angulo):
    radianes = np.radians(angulo)
    matriz_rotacion = np.array([[np.cos(radianes), -np.sin(radianes)],
                                [np.sin(radianes), np.cos(radianes)]])
    figura_rotada = np.dot(figura, matriz_rotacion)
    return figura_rotada

# Crear subplots
fig, axs = plt.subplots(2, 3, figsize=(15, 10))

# Títulos de las figuras
titulos = ["Cuadrado", "Triángulo", "Rectángulo", "Pentágono", "Romboide"]

# Solicitar al usuario el ángulo de rotación para cada figura
angulos = {}
for nombre in figuras.keys():
    angulos[nombre] = float(input(f"Introduce el ángulo de rotación para {nombre}: "))

# Graficar las figuras originales y rotadas
for i, (nombre, figura) in enumerate(figuras.items()):
    # Índices de los subplots
    row, col = divmod(i, 3)
    
    # Graficar figura original
    axs[row, col].plot(figura[:, 0], figura[:, 1], label='Original')
    
    # Rotar la figura
    figura_rotada = rotar_figura(figura, angulos[nombre])
    
    # Graficar figura rotada
    axs[row, col].plot(figura_rotada[:, 0], figura_rotada[:, 1], label=f'Rotada {angulos[nombre]}°')
    
    # Ajustar título y leyenda
    axs[row, col].set_title(titulos[i])
    axs[row, col].legend()

# Ocultar el subplot vacío
axs[1, 2].axis('off')

plt.tight_layout()
plt.show()

