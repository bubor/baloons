__author__ = 'kuba'
from math import *
import pygame

def calculateBox2DValue(initialValue):
    return float(initialValue) / 400.0


def calculatePygameValue(initialValue):
    return int(initialValue * 400.0)


def distanceBetweenPoints(point1, point2):
    xx = point1[0] - point2[0]
    yy = point1[1] - point2[1]
    return sqrt(pow(xx, 2) + pow(yy, 2))