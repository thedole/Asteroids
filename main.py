# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    modules = {
        "mixer": pygame.mixer,
        "display": pygame.display,
        "font": pygame.font,
        "event": pygame.event,
        "joystick": pygame.joystick
        }
    
    for name, module in modules.items():
        try:
            print(f"---- Trying to initialize: {name}")
            module.init()
        except Exception as e:
            print(f"initialization failed!\n")

    print(pygame.init())
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)


    player = Player(x, y)
    asteroid_field = AsteroidField()

    # -------- Game loop --------
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(0)
        updateable.update(dt)

        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game over!")
                sys.exit(1)

            for shot in shots:
                if asteroid.is_colliding(shot):
                    shot.kill()
                    asteroid.got_shot()

        for o in drawable:
            o.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()
