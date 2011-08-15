__author__ = 'kuba'
import pygame
import utils
from Box2D import *

class Balloon:
    def __init__(self, world, coordinates, radius):
        self.body = world.CreateDynamicBody()
        self.body.position = [utils.calculateBox2DValue(coordinates[0]), utils.calculateBox2DValue(coordinates[1])]
        self.body.active = False
        self.shape = b2CircleShape()
        self.shape.pos = (utils.calculateBox2DValue(0), utils.calculateBox2DValue(0))
        self.shape.radius = utils.calculateBox2DValue(radius)

        self.fixtureDef = b2FixtureDef()
        self.fixtureDef.shape = self.shape
        self.fixtureDef.friction = 0.1
        self.fixtureDef.density = 1
        self.fixtureDef.restitution = 0.5
        self.myFixture = None

    def draw(self, screen):
        color = pygame.Color(56, 159, 191, 200)
        position = self.getPosition()
        radius = utils.calculatePygameValue(self.shape.radius)
        pygame.draw.circle(screen, color, position, radius)

    def getPosition(self):
        return [utils.calculatePygameValue(self.body.position[0]), utils.calculatePygameValue(self.body.position[1])]

    def getRadius(self):
        return utils.calculatePygameValue(self.shape.radius)