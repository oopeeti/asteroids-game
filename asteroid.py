import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):            
        self.kill()
        
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        # randomize the angle of the split
        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        splitted_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        splitted_asteroid_1.velocity = a * 1.2
        
        splitted_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)      
        splitted_asteroid_2.velocity = b * 1.2
