import os
import pygame
from pygame.sprite import Sprite


WIDTH, HEIGHT = 800, 600

COLOR_WHITE = (255, 255, 255)
COLOR_BG = (255, 200, 50)

FPS = 60

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

SIZE = (24, 24)
CAT_IMAGE = pygame.image.load(os.path.join("assets", "cat.png"))
CAT = pygame.transform.scale(CAT_IMAGE, SIZE)
FISH_IMAGE = pygame.image.load(os.path.join("assets", "fish.png"))
FISH = pygame.transform.scale(FISH_IMAGE, SIZE)

MAP = pygame.Rect((WIDTH - 480) / 2, 100, 480, 480)

SPEED = 3


def update_screen(cat, fish):
    SCREEN.fill(COLOR_WHITE)
    pygame.draw.rect(SCREEN, COLOR_BG, MAP)
    SCREEN.blit(CAT, (cat.x, cat.y))
    SCREEN.blit(FISH, (fish.x, fish.y))
    pygame.display.flip()


def main():
    cat = pygame.Rect(20, 20, *SIZE)
    fish = pygame.Rect(120, 20, *SIZE)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            cat.x -= SPEED
        if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            cat.x += SPEED
        if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
            cat.y -= SPEED
        if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
            cat.y += SPEED

        update_screen(cat, fish)

        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
