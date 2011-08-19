__author__ = 'kuba'
from Box2D import *
import utils
import pygame
import random

class Food:
    def __init__(self, world):
        self.world = world
        self.pieces_of_food = list()

    def createPieceOfFood(self, position, radius):
        piece = self.world.CreateDynamicBody()
        piece.position = position
        piece_shape = b2CircleShape()
        piece_shape.pos = [0,0]
        piece_shape.radius = utils.calculateBox2DValue(radius)
        piece_fixture = b2FixtureDef()
        piece_fixture.shape = piece_shape
        piece.CreateFixture(piece_fixture)
        self.pieces_of_food.append(piece)

    def createLeftPipeFood(self):
        if(random.randint(0, 20) <= 1):
            return 
        self.createPieceOfFood([utils.calculateBox2DValue(-20), utils.calculateBox2DValue(100)], 4)


    def draw(self, screen):
        for piece in self.pieces_of_food:
            color = pygame.Color(0, 0, 0)
            position = piece.position
            position = [utils.calculatePygameValue(position[0]), utils.calculatePygameValue(position[1])]
            radius = utils.calculatePygameValue(piece.fixtures[0].shape.radius)
            pygame.draw.circle(screen, color, position, radius)

    def updateScore(self):
        i = 0
        score = 0
        while i < len(self.pieces_of_food):
            position = self.pieces_of_food[i].position
            position = [utils.calculatePygameValue(position[0]), utils.calculatePygameValue(position[1])]
            if position[0] > 347 and position[0] < 445 and position[1] > 600:
                score += 1
                self.removePieceAt(i)
            else:
                i += 1
        return score


    def removeOutsiders(self):
        i = 0
        while i < len(self.pieces_of_food):
            position = self.pieces_of_food[i].position
            position = [utils.calculatePygameValue(position[0]), utils.calculatePygameValue(position[1])]
            if position[1] > 600:
                self.removePieceAt(i)
            else:
                i += 1

    def removePiece(self, piece):
        self.world.DestroyBody(piece)
        self.pieces_of_food.remove(piece)

    def removePieceAt(self, index):
        self.world.DestroyBody(self.pieces_of_food[index])
        self.pieces_of_food.pop(index)