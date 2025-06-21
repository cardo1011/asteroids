import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    timer = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    new_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    new_asteroid_field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots)


    while True:
        screen.fill("black")

        for ast in asteroids:
            if new_player.collision_check(ast):
                print("Game over!")
                sys.exit(0)

        updatable.update(dt)
        shots.update(dt)

        for player in drawable:
            player.draw(screen)
        
        for shot in shots:
            shot.draw(screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
            
        dt = timer.tick(60) / 1000
        

    

if __name__ == "__main__":
    main()