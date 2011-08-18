__author__ = 'kuba'
from Box2D import *
import utils
import pygame

class Pipe:
    def __init__(self, world, positions):
        #todo: position to be used below!
        self.shapes = b2EdgeShape()
        self.shapes.vertices = [(utils.calculateBox2DValue(0), utils.calculateBox2DValue(0)), (utils.calculateBox2DValue(200), utils.calculateBox2DValue(50))]
        self.body = world.CreateStaticBody()
        self.body.position = (utils.calculateBox2DValue(positions[0]), utils.calculateBox2DValue(positions[1]))
        self.fixture = b2FixtureDef()
        self.fixture.shape = self.shapes
        self.fixture.friction = 0.1
        self.body.CreateFixture(self.fixture)

    def draw(self, screen):
        initial_position = [utils.calculatePygameValue(self.body.position[0]), utils.calculatePygameValue(self.body.position[1])]
        end_position = [initial_position[0] + utils.calculatePygameValue(self.shapes.vertices[1][0]), initial_position[1] + utils.calculatePygameValue(self.shapes.vertices[1][1])]
        pygame.draw.line(screen, [0,0,0], initial_position, end_position, 1)