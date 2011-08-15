__author__ = 'kuba'
import pygame
import utils
from Box2D import *

class Balloon:
    def __init__(self, world, coordinates, radius):
        self.body = world.CreateDynamicBody()
        self.body.position = [utils.calculateBox2DValue(coordinates[0]), utils.calculateBox2DValue(coordinates[1])]
        self.shape = b2CircleShape()
        self.shape.pos = (utils.calculateBox2DValue(-radius), utils.calculateBox2DValue(-radius))
        self.shape.radius = utils.calculateBox2DValue(radius)
        fixtureDef = b2FixtureDef()
        fixtureDef.shape = self.shape
        fixtureDef.friction = 0.1
        fixtureDef.density = 1
        self.body.CreateFixture(fixtureDef)

    def draw(self, screen):
        color = pygame.Color(56, 159, 191, 200)
        position = [utils.calculatePygameValue(self.body.position[0]), utils.calculatePygameValue(self.body.position[1])]
        radius = utils.calculatePygameValue(self.shape.radius)
        pygame.draw.circle(screen, color, position, radius)