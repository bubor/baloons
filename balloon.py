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
        color = pygame.Color(56, 159, 191)
        position = self.getPosition()
        radius = utils.calculatePygameValue(self.shape.radius)
        surface = pygame.Surface((2*radius, 2*radius))
        surface.fill((0,255,0))
        surface.set_colorkey((0,255,0))
        surface.set_alpha(200)
        pygame.draw.circle(surface, color, [radius,radius], radius)
        screen.blit(surface, [position[0]-radius, position[1]-radius, 2*radius, 2*radius])

    def getPosition(self):
        return [utils.calculatePygameValue(self.body.position[0]), utils.calculatePygameValue(self.body.position[1])]

    def getRadius(self):
        return utils.calculatePygameValue(self.shape.radius)

    def destroyBody(self, world):
        self.body.active = False
        world.DestroyBody(self.body)

    def reloadFixture(self):
        self.body.DestroyFixture(self.myFixture)
        self.myFixture = self.body.CreateFixture(self.fixtureDef)