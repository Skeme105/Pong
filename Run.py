import pygame, sys
from player1 import Player1
from player2 import Player2
from ball import Ball

class Game(object):

    def __init__(self):

        #Config
        self.tps_max = 100.0

        #Initialization
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        self.player = Player1(self)
        self.playerII = Player2(self)
        self.ball = Ball(self)

        while True:

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max

            # Drawing
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()


    def tick(self):
        self.player.tick()
        self.playerII.tick()
        self.ball.tick()

    def draw(self):
        self.player.draw()
        self.playerII.draw()
        self.ball.draw()








if __name__ == "__main__":
    Game()

