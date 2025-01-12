import pygame
from constants import *
from circleshape import CircleShape


class Bullet(CircleShape):
    def __init__(self, x, y, direction):
        self.direction = direction
        super().__init__(x, y, BULLET_RADIUS)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)
        
    def update(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.direction)
        self.position += forward * BULLET_SPEED * dt
        