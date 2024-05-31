import pygame
import sys

# Programa de muestreo de colores
# Elaborado por Edgar Israel Trejo Vazquez y Denisse Delgadillo Pinedo
# Nota: Para usar este programa es necesario tener instalado Python y la librebria Pygame

# Dimensiones de la ventana
WIDTH = 1366
HEIGHT = 768

# Inicializar pygame
pygame.init()

# Crear la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Colores RGB")

# Colores
BLACK = (0, 0, 0)

# Coordenadas del cuadrado
x = 0
y = 0

# Lista de incrementos permitidos
incrementos_permitidos = [1, 2, 4, 8, 16]

# Solicitar al usuario el incremento en la suma de los valores de color
incremento = None
while incremento not in incrementos_permitidos:
    try:
        incremento = int(input("Ingrese el incremento para la suma de los valores de color (1, 2, 4, 8, 16): "))
    except ValueError:
        print("Por favor, ingrese un número de los que se muestran.")
        pass

# Inicializar contador de píxeles pintados
pixels_pintados = 0

# Ciclo para cambiar los colores
for r in range(0, 256, incremento):
    for g in range(0, 256, incremento):
        for b in range(0, 256, incremento):
            # Actualizar el color actual
            current_color = (r, g, b)

            # Dibujar el cuadrado
            pygame.draw.rect(screen, current_color, (x, y, 3, 3))
            pygame.display.update()

            # Incrementar el contador de píxeles pintados
            pixels_pintados += 1

            # Mostrar el contador RGB y de píxeles pintados en la consola
            print(f"RGB: {r}, {g}, {b} | Píxeles pintados: {pixels_pintados}", end='\r', flush=True)

            # Pequeño retraso para mostrar los colores más rápido
            pygame.time.delay(1)

            # Manejar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Mover a la siguiente posición
            x += 3
            # Si llega al borde derecho, saltar de línea
            if x >= WIDTH:
                x = 0
                y += 3

            # Si llega al borde inferior, salir del bucle
            if y >= HEIGHT:
                break
        else:
            continue
        break
    else:
        continue
    break

# Mantener la ventana abierta
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
