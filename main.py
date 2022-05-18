import pygame, time, random

pygame.init()

width = 960
height = 540

main_window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Main Window!")
fps = pygame.time.Clock()
main_window.fill((255,0,0))

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

colours = [red, green, blue]

rectangles = []

for i in range (1, 1000):
    rectangle = pygame.Rect(random.randint(1, 960), random.randint(1, 540), 150, 170)
    rectangles.append(rectangle)

i = 0

while i < len(rectangles):
    pygame.draw.rect(main_window, colours[random.randint(0,2)], rectangles[i])
    i +=1

j = True

while j:
    pygame.display.update()#updates the pyame window
    for event in pygame.event.get(): #if the pygame window is exited - the loop breaks and the Quit() function is run
        if event.type == pygame.QUIT:
            j = False
