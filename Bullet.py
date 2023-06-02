import pygame

from GameObject import GameObject, bullets, imageBullets, WIDTH, HEIGHT, objects, shout, window
from Smoke import Smoke


class Bullet(GameObject):
    def __init__(self, parent, px, py, dx, dy, damage):
        bullets.append(self)
        self.px = px
        self.py = py
        self.dx = dx
        self.dy = dy
        self.damage = damage
        self.parent = parent

        self.image = pygame.transform.rotate(imageBullets[self.parent.order - 1], -self.parent.direct * 90)
        self.rect = self.image.get_rect(center=self.parent.rect.center)

    def update(self, music_on):
        self.image = pygame.transform.rotate(imageBullets[self.parent.order - 1], -self.parent.direct * 90)
        self.rect = self.image.get_rect(center=(self.px, self.py))
        self.px += self.dx
        self.py += self.dy

        # if bullet is out of window
        if self.px < 0 or self.px > WIDTH or self.py < 0 or self.py > HEIGHT:
            bullets.remove(self)
        else:
            for obj in objects:
                # if bullet hits the object and its not the same object where bullet starts
                if obj != self.parent and obj.type != 'smoke' and obj.rect.collidepoint(self.px, self.py):
                    if obj.type == 'tank':
                        state = obj.damage(self.damage, music_on)
                        if state == 'game_over':
                            return state
                    elif obj.type == 'bonus':
                        obj.damage(self.parent)
                    else:
                        obj.damage(self.damage)
                    bullets.remove(self)
                    if obj.type != 'bonus':
                        Smoke(self.px, self.py)
                    if music_on:
                        shout.play()
                    break

    def draw(self):
        window.blit(self.image, self.rect)
