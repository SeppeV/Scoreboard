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

achtergrond = pygame.image.load("achtergrond.png")
achtergrond = pygame.transform.smoothscale(achtergrond,(800, 600))
maaseik = pygame.image.load("maaseiktr.png")
maaseik = pygame.transform.smoothscale(maaseik,(200, 150))
Roeselare= pygame.image.load("roeselaretr.png")
Roeselare = pygame.transform.smoothscale(Roeselare,(200, 150))

# TODO: Laad hier je font
# font = ...

score1 = 0
score2 = 0
thuisset = 0
uitset = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                running = False
            elif event.key == pygame.K_LEFT:
                score1 += 1
                if score1 >= 25:
                    if score2 < score1 - 1:
                        score1 = 0
                        score2 = 0
                        thuisset += 1
                if uitset == 2 and thuisset == 2:
                    if score2 == 15:
                        if score2 < score1 - 1:
                            thuisset += 1
            elif event.key == pygame.K_RIGHT:
                score2 += 1
                if score2 >= 25:
                    if score1 < score2 - 1:
                        score1 = 0
                        score2 = 0
                        uitset += 1
                if uitset == 2 and thuisset == 2:
                    if score2 == 15:
                        if score1 < score2 - 1:
                            uitset += 1
            elif event.key == pygame.K_r:
                score1 = 0
                thuisset = 0
                score2 = 0
                uitset = 0




    screen.fill("white")
    screen.blit(achtergrond, (0, 0))
    screen.blit(maaseik, (130, 70))
    screen.blit(Roeselare, (470, 70))


    font = pygame.font.SysFont("comicsansms", 45)
    text = font.render(f"{score1}", True, "black")
    h = text.get_height()
    w = text.get_width()
    screen.blit(text,(WIDTH/4-w/2 ,HEIGHT/1.5-h/2))



    font = pygame.font.SysFont("comicsansms", 45)
    text = font.render(f"{score2}", True, "black")
    h = text.get_height()
    w = text.get_width()
    screen.blit(text, (WIDTH / 1.35 - w / 3, HEIGHT / 1.5 - h / 2))

    font = pygame.font.SysFont("comicsansms", 24)
    text = font.render(f"{thuisset}", True, "black")
    h = text.get_height()
    w = text.get_width()
    screen.blit(text, (WIDTH / 4 - w / 3, HEIGHT / 1.25 - h / 2))


    font = pygame.font.SysFont("comicsansms", 24)
    text = font.render(f"{uitset}", True, "black")
    h = text.get_height()
    w = text.get_width()
    screen.blit(text, (WIDTH / 1.35 - w / 3, HEIGHT / 1.25 - h / 2))

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