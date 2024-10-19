import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
import sys

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    dt = 0 # delta

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for item in updatable:
            item.update(dt)
            for asteroid in asteroids:
                if player.collision_check(asteroid):
                    print("Game Over")
                    sys.exit()

        screen.fill(000000)
        
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        dt = (clock.tick(60))/1000
        

if __name__ == "__main__":
    main()