__author__ = 'kuba'
import pygame
import balloon
import pipe
import utils
import food
from Box2D import *

pygame.init()
pygame.init()
size = [800, 600]
screen = pygame.display.set_mode(size)

pygame.mixer.init()
pygame.font.init()
font = pygame.font.Font('gfx/font.ttf', 15)
rabbit = pygame.image.load('gfx/rabbit.png').convert()
mouth = pygame.image.load('gfx/mouth.png').convert()
blow_sound = pygame.mixer.Sound('sound/blow.ogg')
blow_sound.set_volume(0.7)
pop_sound = pygame.mixer.Sound('sound/pop.ogg')
pygame.mixer.music.load('sound/audio.ogg')
pygame.mixer.music.play(-1)

mouth.set_colorkey([0,255,0])

world_for_bubbles = b2World()
world_for_bubbles.gravity = (0, -1)

world_for_food = b2World()
world_for_food.gravity = (0, 10)
left_pipe = pipe.Pipe(world_for_food, [-50, 400])
food_machine = food.Food(world_for_food)

pygame.display.set_caption("Balloons")
done = False

score = 0
best_score = int(open('scrs', 'r').readline())
clock = pygame.time.Clock()
timeStep = 1.0 / 60
is_balloon_growing = False
is_balloon_shrinking = False

start_time = pygame.time.get_ticks()

balloons = list()
while done == False:
    food_machine.createLeftPipeFood()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    mouse_keys = pygame.mouse.get_pressed()

    #balloons growing
    if mouse_keys[0] and not is_balloon_growing:
        growing_balloon_coordinates = pygame.mouse.get_pos()
        balloons.append(balloon.Balloon(world_for_bubbles, growing_balloon_coordinates, 1))
        is_balloon_growing = True
        blow_sound.play()
    elif is_balloon_growing and mouse_keys[0] == 0:
        is_balloon_growing = False
        blow_sound.stop()
        balloons[-1].myFixture = balloons[-1].body.CreateFixture(balloons[-1].fixtureDef)
        balloons[-1].body.active = True
        balloons[-1].getFoodInside(food_machine)
    elif is_balloon_growing and mouse_keys[0]:
        balloons[-1].shape.radius += utils.calculateBox2DValue(4)

    world_for_bubbles.Step(timeStep, 6, 2)
    world_for_bubbles.ClearForces()
    world_for_food.Step(timeStep, 6, 2)
    world_for_food.ClearForces()

    #balloons shrinking
    if mouse_keys[2] and not is_balloon_growing and not is_balloon_shrinking:
        shrinking_balloon_coordinates = pygame.mouse.get_pos()
        for i in range(len(balloons)):
            if utils.distanceBetweenPoints(balloons[i].getPosition(), shrinking_balloon_coordinates) < balloons[i].getRadius():
                shrinking_balloon = balloons[i]
                is_balloon_shrinking = True
    if mouse_keys[2] and is_balloon_shrinking and shrinking_balloon != None:
        shrinking_balloon.shape.radius -= utils.calculateBox2DValue(4)
        shrinking_balloon.reloadFixture()
        if(shrinking_balloon.getRadius() <= 1):
            shrinking_balloon.releaseAshes(food_machine)
            shrinking_balloon.destroyBody(world_for_bubbles)
            balloons.remove(shrinking_balloon)
            is_balloon_shrinking = False
            pop_sound.play()
    else:
        shrinking_balloon = None
    if not mouse_keys[2]:
        is_balloon_shrinking = False

    for element in balloons:
        element_position = element.getPosition()
        upper_board = [element_position[0], 0]
        if element_position[1] < 0 and utils.distanceBetweenPoints(element_position, upper_board) >= element.getRadius():
            element.destroyBody(world_for_bubbles)
            if(shrinking_balloon == element):
                shrinking_element = None
                is_balloon_shrinking = False
            balloons.remove(element)

    screen.fill((255, 255, 255))
    screen.blit(rabbit, [300, 400, 200, 200])
    text = font.render('Score: ' + str(score), True, [50, 50, 150])
    screen.blit(text, [650, 550])
    text = font.render('Best:    ' + str(best_score), True, [50, 50, 150])
    screen.blit(text, [650, 565])
    end_time = pygame.time.get_ticks()
    seconds = (end_time - start_time) / 1000
    if(seconds == 60):
        if(score > best_score):
            file = open('scrs', 'w+')
            file.write(str(score))
            text = font.render('New personal best!', True, [50, 150, 50])
            screen.blit(text, [320, 300])
        text = font.render('Time:   ' + str(seconds), True, [150, 50, 50])
        screen.blit(text, [650, 580])
        pygame.display.flip()
        pygame.time.wait(1000)
        done = True
        continue
    text = font.render('Time:   ' + str(seconds), True, [50, 50, 150])
    screen.blit(text, [650, 580])
    for element in balloons:
        element.draw(screen)
    food_machine.draw(screen)
    left_pipe.draw(screen)
    screen.blit(mouth, [347, 540, 98, 60])
    score += food_machine.updateScore()
    food_machine.removeOutsiders()
    clock.tick(20)
    pygame.display.flip()

pygame.quit()