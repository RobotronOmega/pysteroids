import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown_timer = 0
        self.score = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def rotate(self, delta):
        self.rotation += PLAYER_TURN_SPEED * delta

    def update(self, delta):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-(delta))
        if keys[pygame.K_d]:
            self.rotate(delta)
        if keys[pygame.K_w]:
            self.move(delta)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.cooldown_timer -= delta

    def move(self, delta):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta
        if self.position.x > SCREEN_WIDTH:
            self.position.x -= SCREEN_WIDTH
        if self.position.x < 0:
            self.position.x += SCREEN_WIDTH
        if self.position.y > SCREEN_HEIGHT:
            self.position.y -= SCREEN_HEIGHT
        if self.position.y < 0:
            self.position.y += SCREEN_HEIGHT


    def shoot(self):
        if self.cooldown_timer <= 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
            self.cooldown_timer = PLAYER_SHOT_COOLDOWN
    
    def increase_score(self, asteroid):
        if asteroid.radius == ASTEROID_MAX_RADIUS:
            self.score += 250
        if asteroid.radius == ASTEROID_MIN_RADIUS * 2:
            self.score += 100
        if asteroid.radius == ASTEROID_MIN_RADIUS:
            self.score += 25