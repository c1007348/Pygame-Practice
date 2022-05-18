import pygame, time

pygame.init()

width = 960
height = 540

main_window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Main Window!")
fps = pygame.time.Clock()
main_window.fill((255,0,0))
rectangle = pygame.Rect(460, 200, 150, 170)
pygame.draw.rect(main_window, (0, 255, 0), rectangle)


i = True

while i:
    pygame.display.update()#updates the pyame window
    for event in pygame.event.get(): #if the pygame window is exited - the loop breaks and the Quit() function is run
        if event.type == pygame.QUIT:
            i = False
