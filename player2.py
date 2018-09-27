import pygame
from pygame.math import Vector2
from ball import Ball

class Player2(object):


    def __init__(self, game):
        self.game = game
        self.speed = 1.3
        self.gravity = 0

        size = self.game.screen.get_size()

        self.pos2 = Vector2(size[0] - 42, size[1]/2)
        self.vel = Vector2(0,0)
        self.acc = Vector2(0,0)




    def add_force(self, force):
        self.acc += force

    def tick(self):

        # Input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_i]:
            self.add_force(Vector2(0,-self.speed))
        if pressed[pygame.K_k]:
            self.add_force(Vector2(0, self.speed))
        if pressed[pygame.K_j]:
            self.add_force(Vector2(-self.speed,0))
        if pressed[pygame.K_l]:
            self.add_force(Vector2(self.speed,0))



        # Physics
        self.vel *= 0.8
        self.vel -= Vector2(0,-self.gravity)

        self.vel += self.acc
        self.pos2 += self.vel
        self.acc *= 0

    def draw(self):

        #Draw player
        pygame.draw.rect(self.game.screen, [0, 200, 100], pygame.Rect(self.pos2[0],self.pos2[1], 30, 100))
