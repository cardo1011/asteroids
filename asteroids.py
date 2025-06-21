from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius) 

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        random_angle = random.uniform(20, 50)
        neg_random_angle = random.uniform(-20, -50)
        new_vel = self.velocity.rotate(random_angle)
        neg_new_vel = self.velocity.rotate(neg_random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_ast = Asteroid(self.position.x, self.position.y, new_radius)
        neg_new_ast = Asteroid(self.position.x, self.position.y, new_radius)

        new_ast.velocity = new_vel * 1.2
        neg_new_ast.velocity = neg_new_vel * 1.2