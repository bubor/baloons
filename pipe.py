__author__ = 'kuba'
from Box2D import *
import utils
import pygame

class Pipe:
    def __init__(self, world, positions):
        self.shapes = b2EdgeShape()
        self.shapes.vertices = [(utils.calculateBox2DValue(0), utils.calculateBox2DValue(0)), (utils.calculateBox2DValue(200), utils.calculateBox2DValue(50))]
        self.body = world.CreateStaticBody()
        self.body.position = (utils.calculateBox2DValue(positions[0]), utils.calculateBox2DValue(positions[1]))
        self.fixture = b2FixtureDef()
        self.fixture.shape = self.shapes
        self.fixture.friction = 0.3
        self.body.CreateFixture(self.fixture)
        self.image = pygame.image.load('gfx/pipe.png').convert_alpha()

    def draw(self, screen):
        position = [utils.calculatePygameValue(self.body.position[0]), utils.calculatePygameValue(self.body.position[1])-80]
        screen.blit(self.image, position)