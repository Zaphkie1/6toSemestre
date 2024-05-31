import pygame

# Elaborado por Edgar Israel Trejo Vazquez y Denisse Delgadillo Pinedo
# Nota: Para usar este programa es necesario tener instalado Python y la librebria Pygame

pygame.init()

window = pygame.display.set_mode((768,768))

pygame.display.set_caption("Circulos en cuadrados")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # pygame.draw.rect(window, (255, 255, 255), (0, 0, 389, 389), 1)
    # pygame.draw.rect(window, (255, 255, 255), (389, 0, 379, 389), 1)
    # pygame.draw.rect(window, (255, 255, 255), (0, 389, 389, 379), 1)
    # pygame.draw.rect(window, (255, 255, 255), (389, 389, 379, 379), 1)

    for y in range(0, 389, 19):
        pygame.draw.line(window, (255, 0, 0), (387, min(387, 194.5 + y)), (max(377 - (min(y // 20, 19)) * 32, 180), 389), 2)
        pygame.draw.line(window, (0, 255, 0), (0, min(387, 194 + y)), (min((min(y // 20, 19)) * 32, 184 - 1), 389), 2)
        pygame.draw.line(window, (0, 0, 255), (0, max(0, 194 - y)), (min((min(y // 20, 19)) * 32, 194 - 1), 0), 2)
        pygame.draw.line(window, (255, 255, 0), (387, max(0, 194-y)), (max(387 - (min(y // 20, 19)) * 32, 194 + 1), 0), 2)

        pygame.draw.line(window, (255, 0, 0), (765, min(387, 194.5 + y)), (max(765 - (min(y // 20, 19)) * 32, 576), 387.5), 2)
        pygame.draw.line(window, (0, 255, 0), (387, min(387, 194 + y)), (min(389 + (min(y // 20, 19)) * 32, 576), 387.5), 2)
        pygame.draw.line(window, (0, 0, 255), (389, max(0, 194 - y)), (min(389 + (min(y // 20, 19)) * 32, 768), -10), 2)
        pygame.draw.line(window, (255, 255, 0), (765, max(-60, 194-y)), (max(765 - (min(y // 20, 19)) * 32, 389), -10), 2)


        for x in range(0, 206, 19):
            pygame.draw.line(window, (255, 0, 0), (389, min(768, 582.5 - x)), (max(378 - (min(x // 20, 19)) * 32, 192.5), 389), 2)
            pygame.draw.line(window, (0, 255, 0), (0, min(768, 582 - x)), (min((min(x // 20, 19)) * 32, 194 - 1), 389), 2)
        pygame.draw.line(window, (0, 0, 255), (0, max(385, 582 + y)), (min((min(y // 20, 19)) * 32, 194 - 1), 768), 2)
        pygame.draw.line(window, (255, 255, 0), (389, max(385, 582 + y)), (max(389 - (min(y // 20, 19)) * 32, 194 + 1), 768), 2)

        for x in range(0, 206, 19):
            pygame.draw.line(window, (255, 0, 0), (765, min(768, 576 - x)), (max(800 - (min(x // 20, 19)) * 32, 0), 390), 2)
            pygame.draw.line(window, (0, 255, 0), (389, min(768, 582.5 - x)), (min(389 + (min(x // 20, 19)) * 32, 576), 389), 2)
        pygame.draw.line(window, (0, 0, 255), (389, max(389, 582 + y)), (min(389 + (min(y // 20, 19)) * 32, 578), 768), 2)
        pygame.draw.line(window, (255, 255, 0), (765, max(389, 578 + y)), (max(800 - (min(y // 20, 19)) * 32, 389), 768), 2)

    pygame.display.flip()

pygame.quit()