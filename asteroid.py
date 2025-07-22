import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, delta):
        self.position += self.velocity * delta

    def split(self):
        old_velocity = self.velocity
        old_position = self.position
        old_radius = self.radius
        self.kill()
        if old_radius <= ASTEROID_MIN_RADIUS:
            return None
        spawn_angle = random.uniform(20, 50)
        spawn_vector_1 = old_velocity.rotate(spawn_angle) * 1.2
        spawn_vector_2 = old_velocity.rotate(-spawn_angle) * 1.2
        asteroid_1 = Asteroid(old_position.x, old_position.y, old_radius - ASTEROID_MIN_RADIUS)
        asteroid_2 = Asteroid(old_position.x, old_position.y, old_radius - ASTEROID_MIN_RADIUS)
        asteroid_1.velocity = spawn_vector_1
        asteroid_2.velocity = spawn_vector_2