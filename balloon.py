__author__ = 'kuba'
import pygame
import utils
from Box2D import *
import random

class Balloon:
    def __init__(self, world, coordinates, radius):
        self.body = world.CreateDynamicBody()
        self.body.position = [utils.calculateBox2DValue(coordinates[0]), utils.calculateBox2DValue(coordinates[1])]
        self.body.active = False
        self.shape = b2CircleShape()
        self.shape.pos = (utils.calculateBox2DValue(0), utils.calculateBox2DValue(0))
        self.shape.radius = utils.calculateBox2DValue(radius)
        self.has_food_inside = False
        self.counter = 0

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
        if(self.has_food_inside):
            half_radius = radius/2
            font = pygame.font.Font('gfx/font.ttf', half_radius)
            size = font.size(str(self.counter))
            text = font.render(str(self.counter), True, [50, 50, 150])
            screen.blit(text, [position[0]-size[0]/2, position[1]-size[1]/2])

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

    def getFoodInside(self, food_machine):
        ball_position = self.getPosition()
        radius = self.getRadius()
        i = 0
        while i < len(food_machine.pieces_of_food):
            piece_position = [utils.calculatePygameValue(food_machine.pieces_of_food[i].position[0]), utils.calculatePygameValue(food_machine.pieces_of_food[i].position[1])]
            if piece_position[0] > 145 and utils.distanceBetweenPoints(ball_position, piece_position) < radius:
                self.counter = self.counter + 1
                self.has_food_inside = True
                food_machine.removePieceAt(i)
            else:
                i = i + 1

    def releaseAshes(self, food_machine):
        for i in range(self.counter):
            position = [self.body.position[0]+random.random()/80, self.body.position[1]+random.random()/80]
            food_machine.createPieceOfFood(position, radius=2)