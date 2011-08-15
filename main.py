__author__ = 'kuba'
import pygame
import balloon
import utils
from Box2D import *

pygame.init()
pygame.init()
size=[800,600]
screen=pygame.display.set_mode(size)

world_for_bubbles = b2World()
world_for_bubbles.gravity = (0, 2)

pygame.display.set_caption("Balloons")
done = False

clock = pygame.time.Clock()
timeStep = 1.0 / 60
is_balloon_growing = False

balloons = list()
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    mouse_keys = pygame.mouse.get_pressed()
    if mouse_keys[0] and not is_balloon_growing:
        growing_balloon_coordinates = pygame.mouse.get_pos()
        print (growing_balloon_coordinates)
        balloons.append(balloon.Balloon(world_for_bubbles, growing_balloon_coordinates, 1))
        is_balloon_growing = True
    elif is_balloon_growing and mouse_keys[0] == 0:
        is_balloon_growing = False
        balloons[-1].body.CreateFixture(balloons[-1].fixtureDef)
        balloons[-1].body.active = True
    elif is_balloon_growing and mouse_keys[0]:
        balloons[-1].shape.radius += utils.calculateBox2DValue(4)

    world_for_bubbles.Step(timeStep, 6, 2)
    world_for_bubbles.ClearForces()
    screen.fill( (255,255,255) )
    for element in balloons:
        element.draw(screen)
    clock.tick(20)
    pygame.display.flip()


pygame.quit()