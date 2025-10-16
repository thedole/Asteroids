# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *

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

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(0)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()
