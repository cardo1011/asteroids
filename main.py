import pygame
from constants import *
from player import Player


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    timer = pygame.time.Clock()
    dt = 0
    new_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    while True:
        screen.fill("black")
        new_player.update(dt)
        new_player.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
        timer.tick(60)
        dt = timer.tick(60) / 1000
        

    

if __name__ == "__main__":
    main()