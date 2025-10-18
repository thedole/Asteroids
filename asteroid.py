import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, kind):
        self.set_kind(kind)
        super().__init__( x, y, self.radius)

    def set_kind(self, kind):
        self.kind = kind
        self.radius = ASTEROID_MIN_RADIUS * kind

    def got_shot(self):
        if self.kind > 1:
            self.set_kind(self.kind - 1)
            self.split()
            return
        
        self.kill()

    def split(self):
        old_velocity = self.velocity
        self.velocity = old_velocity.rotate(ASTEROID_SPLIT_ANGLE)
        new_asteroid = Asteroid(self.position.x, self.position.y, self.kind)
        new_asteroid.velocity = old_velocity.rotate(-ASTEROID_SPLIT_ANGLE)
        
    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color("white"), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt