__author__ = 'kuba'
import pygame

pygame.init()
pygame.init()
size=[800,600]
screen=pygame.display.set_mode(size)

pygame.display.set_caption("My Game")
done = False

clock = pygame.time.Clock()
is_balloon_growing = False

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    mouse_keys = pygame.mouse.get_pressed()
    if mouse_keys[0] and not is_balloon_growing:
        growing_balloon_coordinates = pygame.mouse.get_pos()
        is_balloon_growing = True
    if is_balloon_growing and mouse_keys[0] == 0:
        is_balloon_growing = False

    screen.fill( (255,255,255) )
    clock.tick(20)
    pygame.display.flip()


pygame.quit()