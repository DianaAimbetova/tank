import random
from random import randint

import pygame

from GameObject import WIDTH, X_PIXEL, Y_PIXEL, objects, X_PIXEL_BLOCK, Y_PIXEL_BLOCK, GameObject, window, imageBlocks


class Block(GameObject):
    def __init__(self, px, py, sizeX, sizeY, level):
        objects.append(self)
        self.type = 'block'

        self.rect = pygame.Rect(px, py, sizeX, sizeY)
        self.level = level
        if level == 0:
            self.health = 1
        elif level == 1:
            self.health = 2

    def update(self):
        pass

    def draw(self, i):
        window.blit(imageBlocks[i], self.rect)

    def damage(self, value):
        self.health -= 1
        if self.health <= 0:
            objects.remove(self)


def draw_random_block():
    for _ in range(50):
        while True:
            x = randint(1, WIDTH // X_PIXEL - 1) * X_PIXEL
            y = randint(1, WIDTH // Y_PIXEL - 1) * Y_PIXEL
            rect = pygame.Rect(x, y, X_PIXEL, Y_PIXEL)
            fined = False
            for obj in objects:
                if rect.colliderect(obj.rect):
                    fined = True
            if not fined: break
        Block(x, y, X_PIXEL_BLOCK, Y_PIXEL_BLOCK, random.randint(0, 1))
