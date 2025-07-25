import pygame
import sys
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    pygame.font.init()
    font = pygame.font.Font("Hyperspace-JvEM.ttf", size=48)
    clock = pygame.time.Clock()
    dt = 0
    gamestate = "play"
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # quit handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        if gamestate == "title":
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]:
                gamestate = "play"
            font.size = 64
            fontsurface = font.render("PYSTEROIDS", True, "white")
            font.size = 48
            fontsurface2 = font.render("PRESS ENTER TO BEGIN", True, "white")
            screen.fill("black")
                    
            screen.blit(fontsurface, (((SCREEN_WIDTH - fontsurface.get_width()) / 2),0))
        
        if gamestate == "play":
            # update
            for item in updatable:
                item.update(dt)

            

            # collisions
            for item in asteroids:
                if item.collide(player):
                    print("Game Over!")
                    sys.exit()
            for item in asteroids:
                for bullet in shots:
                    if item.collide(bullet):
                        player.increase_score(item)
                        item.split()
                        bullet.kill()

            # draw  
            fontsurface = font.render(f"Score: {player.score}", True, "white")
            screen.fill("black")
            
            for item in drawable:
                item.draw(screen)
            screen.blit(fontsurface, (((SCREEN_WIDTH - fontsurface.get_width()) / 2),0))

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
