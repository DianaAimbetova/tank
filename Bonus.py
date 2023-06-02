from random import randint, random

import pygame

from GameObject import GameObject, objects, imageBonuses, window, X_PIXEL, WIDTH, Y_PIXEL

X_PIXEL_STAR = 32
Y_PIXEL_STAR = 32


class Bonus(GameObject):
    def __init__(self, px, py, sizeX, sizeY, bonus_type):
        objects.append(self)
        self.type = 'bonus'
        self.rect = pygame.Rect(px, py, sizeX, sizeY)
        self.bonus_type = bonus_type

    def update(self):
        pass

    def draw(self):
        window.blit(imageBonuses[self.bonus_type], self.rect)

    def damage(self, tank):
        pass


def draw_random_stars():
    for _ in range(5):
        while True:
            x = randint(1, WIDTH // X_PIXEL - 1) * X_PIXEL
            y = randint(1, WIDTH // Y_PIXEL - 1) * Y_PIXEL
            rect = pygame.Rect(x, y, X_PIXEL, Y_PIXEL)
            fined = False
            for obj in objects:
                if rect.colliderect(obj.rect):
                    fined = True
            if not fined: break
        Bonus(x, y, X_PIXEL_STAR, Y_PIXEL_STAR, randint(0, 1))
