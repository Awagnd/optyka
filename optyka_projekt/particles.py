import pygame.draw
import random
import math
class Particle:
    def __init__(self, x, y, opacity, colors, angle,v):
        self.x = x
        self.y = y
        self.opacity = opacity
        self.colors = colors
        self.angle=math.radians(angle)
        self.parpop=False
        self.v = v
    def fading(self):

        self.colors = (int(max(0, self.colors[0] - self.opacity)), int(max(0, self.colors[1] - self.opacity)),
                       int(max(0, self.colors[2] - self.opacity)))

    def move(self):
        self.x += math.sin(self.angle)*self.v
        self.y += math.cos(self.angle)*self.v

    def draw(self, scene):
        if self.colors[0] > 0 and self.colors[1] > 0 and self.colors[2] > 0:
            pygame.draw.circle(scene, (self.colors[0], self.colors[1], self.colors[2], self.opacity), (self.x, self.y),
                               10)
        else:
            self.parpop = True
