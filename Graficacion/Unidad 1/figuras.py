import pygame

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la ventana
width = 800
height = 600

# Crear la ventana
window = pygame.display.set_mode((width, height))

# Color blanco y color rojo (para objetos trasladados)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Lista de objetos (en este caso, rectángulos)
objects = []

# Bucle principal del juego
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar la ventana con color blanco
    window.fill(WHITE)

    # Dibujar los objetos originales
    for obj in objects:
        pygame.draw.rect(window, obj['color'], obj['rect'])

    # Actualizar la ventana
    pygame.display.update()

    # Obtener la entrada del usuario para las coordenadas y la distancia de traslación
    if len(objects) < 5:
        x = int(input("Ingrese la coordenada x del objeto: "))
        y = int(input("Ingrese la coordenada y del objeto: "))
        dx = int(input("Ingrese la distancia de traslación en x: "))
        dy = int(input("Ingrese la distancia de traslación en y: "))

        # Crear el objeto
        obj_rect = pygame.Rect(x, y, 50, 50)  # Tamaño del objeto (ancho, alto)
        obj = {'rect': obj_rect, 'color': WHITE}  # Objeto con color blanco
        objects.append(obj)

        # Crear el objeto trasladado
        obj_rect_traslado = obj_rect.move(dx, dy)
        obj_traslado = {'rect': obj_rect_traslado, 'color': RED}  # Objeto trasladado con color rojo
        objects.append(obj_traslado)

# Cerrar Pygame
pygame.quit()
