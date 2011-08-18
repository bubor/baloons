__author__ = 'kuba'
from Box2D import *
import utils
import pygame
import random

class Food:
    def __init__(self, world):
        self.world = world
        self.pieces_of_food = list()

    def createLeftPipeFood(self):
        if(random.randint(0, 20) <= 1):
            return 
        piece = self.world.CreateDynamicBody()
        piece.position = [utils.calculateBox2DValue(-20), utils.calculateBox2DValue(100)]
        piece_shape = b2CircleShape()
        piece_shape.pos = [0,0]
        piece_shape.radius = utils.calculateBox2DValue(4)
        piece_fixture = b2FixtureDef()
        piece_fixture.shape = piece_shape
        piece.CreateFixture(piece_fixture)
        self.pieces_of_food.append(piece)

    def draw(self, screen):
        for piece in self.pieces_of_food:
            color = pygame.Color(0, 0, 0)
            position = piece.position
            position = [utils.calculatePygameValue(position[0]), utils.calculatePygameValue(position[1])]
            radius = utils.calculatePygameValue(piece.fixtures[0].shape.radius)
            pygame.draw.circle(screen, color, position, radius)
        