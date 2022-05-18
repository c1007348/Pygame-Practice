import pygame, time, random

pygame.init()

width = 960
height = 540

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Main Window")
fps = pygame.time.Clock()
window.fill((180,0,0))

sprites = []

for i in range (1, 30):
    test_sprite = pygame.image.load("ready_1.png")
    sprite_new = pygame.transform.scale(test_sprite, (200, 200))
    sprites.append(sprite_new)

i = 0

while i < len(sprites):
    window.blit(sprites[i], (random.randint(1, 800), random.randint(1, 340)))
    i += 1

j = True

while j:
    pygame.display.update()#updates the pyame window
    for event in pygame.event.get(): #if the pygame window is exited - the loop breaks and the Quit() function is run
        if event.type == pygame.QUIT:
            j = False
