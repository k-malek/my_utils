import pygame as pg

class Obstacle:
    OBSTACLE_POS= 13,22
    OBSTACLE_SIZE = 1

    def __init__(self,game,pos=OBSTACLE_POS,size=OBSTACLE_SIZE):
        self.game=game
        self.x,self.y = pos
        self.size = size
        self.hitbox = [self.x,self.y,self.size]

    def draw(self):
        pg.draw.rect(self.game.screen,'darkgrey', (self.x*self.game.scale,self.y*self.game.scale,self.size*self.game.scale,self.size*self.game.scale),0)

    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x),int(self.y)