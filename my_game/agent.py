import pygame as pg
import math

class Agent:
    AGENT_POS = 1.5,5
    AGENT_ANGLE = 0
    AGENT_SPEED = 0.003
    AGENT_ROT_SPEED = 0.002
    AGENT_COLOR='green'

    def __init__(self,game,agent_color=AGENT_COLOR, random_pos=False):
        self.game = game
        if random_pos:
            #create random position gen
            pass
        else:
            self.x, self.y = Agent.AGENT_POS
        self.angle = Agent.AGENT_ANGLE
        self.speed = Agent.AGENT_SPEED * 100/self.game.scale
        self.color = agent_color

    def movement(self):
        sin_ang = math.sin(self.angle)
        cos_ang = math.cos(self.angle)
        dx,dy = 0,0
        speed = self.speed * self.game.delta_time
        speed_sin = speed * sin_ang
        speed_cos = speed * cos_ang

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_LEFT]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_RIGHT]:
            dx += -speed_sin
            dy += speed_cos

        free_to_go=True

        for obstacle in self.game.obstacles:
            if self.check_collision(obstacle,dx,dy):
                free_to_go=False
        
        if free_to_go:
            self.x+=dx
            self.y+=dy

        if keys[pg.K_a]:
            self.angle -= Agent.AGENT_ROT_SPEED * self.game.delta_time
        if keys[pg.K_d]:
            self.angle += Agent.AGENT_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau

    def check_collision(self,object,dx,dy):
        return int(self.x+dx) in range(object.map_pos[0],object.map_pos[0]+object.size) and int(self.y+dy) in range(object.map_pos[1],object.map_pos[1]+object.size)


    def draw(self):
        pg.draw.line(self.game.screen, 'yellow', (self.x*self.game.scale, self.y*self.game.scale),
                     (self.x *self.game.scale + self.game.screen.get_width() * math.cos(self.angle),
                      self.y *self.game.scale + self.game.screen.get_width() * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, self.color, (self.x *self.game.scale , self.y *self.game.scale), 15)

    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x),int(self.y)


