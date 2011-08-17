__author__ = 'kuba'
import pygame
import balloon
import utils
from Box2D import *

pygame.init()
pygame.init()
size = [800, 600]
screen = pygame.display.set_mode(size)

world_for_bubbles = b2World()
world_for_bubbles.gravity = (0, -1)

pygame.display.set_caption("Balloons")
done = False

clock = pygame.time.Clock()
timeStep = 1.0 / 60
is_balloon_growing = False
is_balloon_shrinking = False

balloons = list()
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    mouse_keys = pygame.mouse.get_pressed()

    #balloons growing
    if mouse_keys[0] and not is_balloon_growing:
        growing_balloon_coordinates = pygame.mouse.get_pos()
        balloons.append(balloon.Balloon(world_for_bubbles, growing_balloon_coordinates, 1))
        is_balloon_growing = True
    elif is_balloon_growing and mouse_keys[0] == 0:
        is_balloon_growing = False
        balloons[-1].myFixture = balloons[-1].body.CreateFixture(balloons[-1].fixtureDef)
        balloons[-1].body.active = True
    elif is_balloon_growing and mouse_keys[0]:
        balloons[-1].shape.radius += utils.calculateBox2DValue(4)

    #balloons shrinking
    if mouse_keys[2] and not is_balloon_growing and not is_balloon_shrinking:
        shrinking_balloon_coordinates = pygame.mouse.get_pos()
        for i in range(len(balloons)):
            if utils.distanceBetweenPoints(balloons[i].getPosition(), shrinking_balloon_coordinates) < balloons[i].getRadius():
                shrinking_balloon = i
                is_balloon_shrinking = True
    if mouse_keys[2] and is_balloon_shrinking:
        balloons[shrinking_balloon].shape.radius -= utils.calculateBox2DValue(4)
        balloons[shrinking_balloon].reloadFixture()
        if(balloons[shrinking_balloon].getRadius() <= 1):
            balloons[shrinking_balloon].destroyBody(world_for_bubbles)
            balloons.pop(shrinking_balloon)
            is_balloon_shrinking = False
    if not mouse_keys[2]:
        is_balloon_shrinking = False

    for element in balloons:
        element_position = element.getPosition()
        upper_board = [element_position[0], 0]
        if element_position[1] < 0 and utils.distanceBetweenPoints(element_position, upper_board) >= element.getRadius():
            element.destroyBody(world_for_bubbles)
            balloons.remove(element)

    world_for_bubbles.Step(timeStep, 6, 2)
    world_for_bubbles.ClearForces()
    screen.fill((255, 255, 255))
    for element in balloons:
        element.draw(screen)
    clock.tick(20)
    pygame.display.flip()

pygame.quit()