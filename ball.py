import pygame
from pygame.math import Vector2

import random

class Ball(object):


    def __init__(self, game):


        self.game = game

        self.choicesy =  [-4, 4]
        self.choicesx =  [-2, 2]
        size = self.game.screen.get_size()


        self.xx = size[0]/2
        self.yy = size[1]/2

        self.dx = (random.choice(self.choicesy))
        self.dy = (random.choice(self.choicesx))


    def tick(self, player1, player2):
        print(player1.pos1)
        print(player2.pos2)
        size = self.game.screen.get_size()
        self.xx += self.dx
        self.yy += self.dy

        if self.yy > size[1] - 50 or self.yy < 0:
            self.dy *= -1


        if self.xx > size[0] or self.xx < -100:
            self.xx = size[0] / 2
            self.yy = size[1] / 2
            self.dx = (random.choice(self.choicesy))
            self.dy = (random.choice(self.choicesx))




    def draw(self):



        #Draw ball
        pygame.draw.ellipse(self.game.screen, [0, 200, 100], [self.xx,self.yy, 50, 50])

