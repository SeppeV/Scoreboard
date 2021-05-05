import pygame

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))





# TODO: Laad hier je font
# font = ...



score1 = 0
score2 = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                score1 += 1
            elif event.key == pygame.K_RIGHT:
                score2 += 1
            elif event.key == pygame.K_r:
                score1 = 0
                score2 = 0


    screen.fill("black")

    font = pygame.font.SysFont("comicsansms", 24)
    text = font.render(f"{score1}-{score2}", True, "white")
    h = text.get_height()
    w = text.get_width()
    screen.blit(text,(WIDTH/2-w/2 ,HEIGHT/2-h/2))

    text = font.render(f"{set1}-{set2}", True, "white")
    h = text.get_height(30)
    w = text.get_width(40)
    screen.blit(text, (WIDTH / 2 - w / 2, HEIGHT / 2 - h / 2))

    label = "Hallo"
    # TODO: Render hier de tekst en toon op het scherm
    # text = ...
    # ...

    pygame.display.flip()
