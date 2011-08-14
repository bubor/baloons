__author__ = 'kuba'
import pygame

class Balloon:
    def __init__(self, coordinates, radius):
        self.coordinates = coordinates
        self.radius = radius

    def draw(self, screen):
        color = pygame.Color(56, 159, 191, 200)
        place_to_draw = [self.coordinates[0], self.coordinates[1]]
        pygame.draw.circle(screen, color, place_to_draw, self.radius)