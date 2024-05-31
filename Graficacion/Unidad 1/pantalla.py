import pygame

# Inicializar Pygame
pygame.init()

# Configurar el tamaño de la ventana
ventana = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("Mi Ventana")

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Generar una línea de color
    pygame.draw.line(ventana, (255, 255, 255), (683, 0), (683, 384), 1)
    pygame.draw.line(ventana, (255, 255, 255), (683, 19), (649, 384), 1)
    pygame.draw.line(ventana, (255, 255, 255), (683, 38), (615, 384), 1)
    pygame.draw.line(ventana, (255, 255, 255), (683, 57), (581, 384), 1)
    pygame.draw.line(ventana, (255, 255, 255), (683, 76), (547, 384), 1)
    pygame.draw.line(ventana, (255, 255, 255), (683, 95), (513, 384), 1)
    pygame.draw.line(ventana, (255, 255, 255), (683, 114), (479, 384), 1)
    pygame.draw.line(ventana, (255, 255, 255), (683, 133), (445, 384), 1)
    pygame.draw.line(ventana, (255, 255, 255), (683, 152), (411, 384), 1)
    pygame.draw.line(ventana, (255, 255, 255), (683, 171), (377, 384), 1)
    pygame.draw.line(ventana, (255, 255, 255), (683, 190), (343, 384), 1)
    pygame.draw.line(ventana, (255, 255, 255), (683, 209), (309, 384), 1)
    pygame.draw.line(ventana, (255, 255, 255), (683, 228), (275, 384), 1)
    pygame.draw.line(ventana, (255, 255, 255), (683, 247), (241, 384), 1)
    pygame.draw.line(ventana, (255, 255, 255), (683, 266), (207, 384), 1)
    pygame.draw.line(ventana, (255, 255, 255), (683, 285), (173, 384), 1)
    pygame.draw.line(ventana, (255, 255, 255), (683, 304), (139, 384), 1)
    pygame.draw.line(ventana, (255, 255, 255), (683, 323), (105, 384), 1)
    pygame.draw.line(ventana, (255, 255, 255), (683, 342), (71, 384), 1)
    pygame.draw.line(ventana, (255, 255, 255), (683, 361), (37, 384), 1)
    pygame.draw.line(ventana, (255, 255, 255), (683, 384), (3, 384), 1)

    #parte inferior izquierda
    pygame.draw.line(ventana, (239, 169, 0), (683, 384), (3, 384), 1)
    pygame.draw.line(ventana, (239, 169, 0), (683, 403), (37, 384), 1)
    pygame.draw.line(ventana, (239, 169, 0), (683, 422), (71, 384), 1)
    pygame.draw.line(ventana, (239, 169, 0), (683, 441), (105, 384), 1)
    pygame.draw.line(ventana, (239, 169, 0), (683, 460), (139, 384), 1)
    pygame.draw.line(ventana, (239, 169, 0), (683, 479), (173, 384), 1)
    pygame.draw.line(ventana, (239, 169, 0), (683, 498), (207, 384), 1)
    pygame.draw.line(ventana, (239, 169, 0), (683, 517), (241, 384), 1)
    pygame.draw.line(ventana, (239, 169, 0), (683, 536), (275, 384), 1)
    pygame.draw.line(ventana, (239, 169, 0), (683, 555), (309, 384), 1)
    pygame.draw.line(ventana, (239, 169, 0), (683, 574), (343, 384), 1)
    pygame.draw.line(ventana, (239, 169, 0), (683, 593), (377, 384), 1)
    pygame.draw.line(ventana, (239, 169, 0), (683, 612), (411, 384), 1)
    pygame.draw.line(ventana, (239, 169, 0), (683, 631), (445, 384), 1)
    pygame.draw.line(ventana, (239, 169, 0), (683, 650), (479, 384), 1)
    pygame.draw.line(ventana, (239, 169, 0), (683, 669), (513, 384), 1)
    pygame.draw.line(ventana, (239, 169, 0), (683, 688), (547, 384), 1)
    pygame.draw.line(ventana, (239, 169, 0), (683, 707), (581, 384), 1)
    pygame.draw.line(ventana, (239, 169, 0), (683, 726), (615, 384), 1)
    pygame.draw.line(ventana, (239, 169, 0), (683, 745), (649, 384), 1)
    pygame.draw.line(ventana, (239, 169, 0), (683, 764), (683, 384), 1)

    #parte superior derecha

    pygame.draw.line(ventana, (87, 35, 100), (683, 0), (720, 384), 1)
    pygame.draw.line(ventana, (87, 35, 100), (683, 19), (754, 384), 1)
    pygame.draw.line(ventana, (87, 35, 100), (683, 38), (788, 384), 1)
    pygame.draw.line(ventana, (87, 35, 100), (683, 57), (822, 384), 1)
    pygame.draw.line(ventana, (87, 35, 100), (683, 76), (856, 384), 1)
    pygame.draw.line(ventana, (87, 35, 100), (683, 95), (890, 384), 1)
    pygame.draw.line(ventana, (87, 35, 100), (683, 114), (924, 384), 1)
    pygame.draw.line(ventana, (87, 35, 100), (683, 133), (958, 384), 1)
    pygame.draw.line(ventana, (87, 35, 100), (683, 152), (992, 384), 1)
    pygame.draw.line(ventana, (87, 35, 100), (683, 171), (1026, 384), 1)
    pygame.draw.line(ventana, (87, 35, 100), (683, 190), (1060, 384), 1)
    pygame.draw.line(ventana, (87, 35, 100), (683, 209), (1094, 384), 1)
    pygame.draw.line(ventana, (87, 35, 100), (683, 228), (1128, 384), 1)
    pygame.draw.line(ventana, (87, 35, 100), (683, 247), (1162, 384), 1)
    pygame.draw.line(ventana, (87, 35, 100), (683, 266), (1196, 384), 1)
    pygame.draw.line(ventana, (87, 35, 100), (683, 285), (1230, 384), 1)
    pygame.draw.line(ventana, (87, 35, 100), (683, 304), (1264, 384), 1)
    pygame.draw.line(ventana, (87, 35, 100), (683, 323), (1298, 384), 1)
    pygame.draw.line(ventana, (87, 35, 100), (683, 342), (1332, 384), 1)
    pygame.draw.line(ventana, (87, 35, 100), (683, 361), (1366, 384), 1)


    #parte inferior izquierda
    pygame.draw.line(ventana, (255, 0, 0), (683, 384), (1366, 384), 1)
    pygame.draw.line(ventana, (255, 0, 0), (683, 403), (1332, 384), 1)
    pygame.draw.line(ventana, (255, 0, 0), (683, 422), (1292, 384), 1)
    pygame.draw.line(ventana, (255, 0, 0), (683, 441), (1258, 384), 1)
    pygame.draw.line(ventana, (255, 0, 0), (683, 460), (1224, 384), 1)
    pygame.draw.line(ventana, (255, 0, 0), (683, 479), (1190, 384), 1)
    pygame.draw.line(ventana, (255, 0, 0), (683, 498), (1156, 384), 1)
    pygame.draw.line(ventana, (255, 0, 0), (683, 517), (1122, 384), 1)
    pygame.draw.line(ventana, (255, 0, 0), (683, 536), (1088, 384), 1)
    pygame.draw.line(ventana, (255, 0, 0), (683, 555), (1054, 384), 1)
    pygame.draw.line(ventana, (255, 0, 0), (683, 574), (1020, 384), 1)
    pygame.draw.line(ventana, (255, 0, 0), (683, 593), (986, 384), 1)
    pygame.draw.line(ventana, (255, 0, 0), (683, 612), (952, 384), 1)
    pygame.draw.line(ventana, (255, 0, 0), (683, 631), (918, 384), 1)
    pygame.draw.line(ventana, (255, 0, 0), (683, 650), (884, 384), 1)
    pygame.draw.line(ventana, (255, 0, 0), (683, 669), (850, 384), 1)
    pygame.draw.line(ventana, (255, 0, 0), (683, 688), (816, 384), 1)
    pygame.draw.line(ventana, (255, 0, 0), (683, 707), (782, 384), 1)
    pygame.draw.line(ventana, (255, 0, 0), (683, 726), (748, 384), 1)
    pygame.draw.line(ventana, (255, 0, 0), (683, 745), (714, 384), 1)
    pygame.draw.line(ventana, (255, 0, 0), (683, 764), (683, 384), 1)


    # Actualizar la ventana
    pygame.display.flip()

# Salir de Pygame
pygame.quit()

