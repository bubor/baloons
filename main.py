__author__ = 'kuba'
import pygame
import balloon
from Box2D import *

pygame.init()
pygame.init()
size=[800,600]
screen=pygame.display.set_mode(size)

world_for_bubbles = b2World()
world_for_bubbles.gravity = (0, 0)

pygame.display.set_caption("Balloons")
done = False

clock = pygame.time.Clock()
is_balloon_growing = False

balloons = None
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    mouse_keys = pygame.mouse.get_pressed()
    if mouse_keys[0] and not is_balloon_growing:
        growing_balloon_coordinates = pygame.mouse.get_pos()
        print (growing_balloon_coordinates)
        balloons = balloon.Balloon(world_for_bubbles, growing_balloon_coordinates, 1)
        is_balloon_growing = True
    elif is_balloon_growing and mouse_keys[0] == 0:
        is_balloon_growing = False
    elif is_balloon_growing and mouse_keys[0]:
        balloons.shape.radius += 4
        print(is_balloon_growing)

    screen.fill( (255,255,255) )
    if balloons:
        balloons.draw(screen)
    clock.tick(20)
    pygame.display.flip()


pygame.quit()