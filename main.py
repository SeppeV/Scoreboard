import pygame

import configparser
config = configparser.ConfigParser()
config.read("config.ini")
ploegnaamA = config["teamA"]["naam"]
print(ploegnaamA)

ploegnaamB = config["teamB"]["naam2"]
print(ploegnaamB)

titel = config["algemeen"]["titel"]
print(titel)

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

maaseik = pygame.image.load("Maaseik.jpg")
Roeselare= pygame.image.load("Knack.jpg")
Roeselare = pygame.transform.smoothscale(Roeselare,(250, 175))

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


    screen.fill("white")
    screen.blit(maaseik, (100, 80))
    screen.blit(Roeselare, (515, 110))

    font = pygame.font.SysFont("comicsansms", 24)
    text = font.render(f"{score1}", True, "black")
    h = text.get_height()
    w = text.get_width()
    screen.blit(text,(WIDTH/4-w/2 ,HEIGHT/1.25-h/2))



    font = pygame.font.SysFont("comicsansms", 24)
    text = font.render(f"{score2}", True, "black")
    h = text.get_height()
    w = text.get_width()
    screen.blit(text, (WIDTH / 1.25 - w / 3, HEIGHT / 1.25 - h / 2))

    font = pygame.font.SysFont("comicsansms", 35)
    text = font.render(f"    {ploegnaamA}              {ploegnaamB}", True, "black")
    h = text.get_height()
    w = text.get_width()
    screen.blit(text, (WIDTH / 3 - w / 3, HEIGHT /  1.75 - h / 2))


    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render(f"{titel}", True, "black")
    h = text.get_height()
    w = text.get_width()
    screen.blit(text, (WIDTH / 2 - w / 2, HEIGHT / 11 - h / 2))

    label = "Hallo"
    # TODO: Render hier de tekst en toon op het scherm
    # text = ...
    # ...

    pygame.display.flip()