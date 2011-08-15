__author__ = 'kuba'
import pygame
from Box2D import *

class Balloon:
    def __init__(self, world, coordinates, radius):
        self.body = world.CreateDynamicBody()
        self.body.position = coordinates
        self.shape = b2CircleShape()
        self.shape.pos = (-radius, -radius)
        self.shape.radius = radius
        fixtureDef = b2FixtureDef()
        fixtureDef.shape = self.shape
        fixtureDef.friction = 0.1
        fixtureDef.density = 1
        self.body.CreateFixture(fixtureDef)

    def draw(self, screen):
        color = pygame.Color(56, 159, 191, 200)
        place_to_draw = [self.body.position[0], self.body.position[1]]
        pygame.draw.circle(screen, color, place_to_draw, self.shape.radius)