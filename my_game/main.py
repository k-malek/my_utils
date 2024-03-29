import pygame as pg
from agent import *
from obstacle import *
import sys

RES = WIDTH,HEIGHT = 1600,900
FPS = 120
SCALE = 25

class Game:
    def __init__(self,scale=SCALE):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.delta_time=1
        self.clock = pg.time.Clock()
        self.scale=scale
        self.new_game()

    def new_game(self):
        self.player=Agent(self)
        self.obstacles=[Obstacle(self),Obstacle(self,(5,5),3)]

    def update(self):
        self.player.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f} {[obstacle.hitbox for obstacle in self.obstacles]}')

    def draw(self):
        self.screen.fill('black')
        self.player.draw()
        for obstacle in self.obstacles:
            obstacle.draw()

    def check_events(self):
            for event in pg.event.get():
                 if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                      pg.quit()
                      sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
     game = Game()
     game.run()