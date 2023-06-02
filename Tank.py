from Bullet import Bullet
from GameObject import GameObject, objects, X_PIXEL, Y_PIXEL, imageTanks, music_on, touch, HEIGHT, WIDTH, DIRECTS, \
    window, fail, bonus_music

import pygame


pygame.init()


class Tank(GameObject):
    def __init__(self, color, x, y, direct, keyList, order):
        objects.append(self)
        self.type = 'tank'

        self.color = color
        self.rect = pygame.Rect(x, y, X_PIXEL, Y_PIXEL)
        self.direct = direct
        self.moveSpeed = 1
        self.health = 3

        self.bulletDamage = 1
        self.bulletSpeed = 10

        self.shotTimer = 0
        self.shotDelay = 60

        self.keyLeft = keyList[0]
        self.keyRight = keyList[1]
        self.keyUp = keyList[2]
        self.keyDown = keyList[3]
        self.keyShoot = keyList[4]

        self.order = order
        self.image = pygame.transform.rotate(imageTanks[self.order - 1], -self.direct * 90)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self, keys, music_on):
        self.image = pygame.transform.rotate(imageTanks[self.order - 1], -self.direct * 90)
        self.rect = self.image.get_rect(center=self.rect.center)
        oldX, oldY = self.rect.topleft
        if keys[self.keyLeft]:
            self.rect.x -= self.moveSpeed
            self.direct = 3
        if keys[self.keyRight]:
            self.rect.x += self.moveSpeed
            self.direct = 1
        if keys[self.keyUp]:
            self.rect.y -= self.moveSpeed
            self.direct = 0
        if keys[self.keyDown]:
            self.rect.y += self.moveSpeed
            self.direct = 2

        # if tank meets block
        for obj in objects:
            if obj.type == 'block' and obj != self:
                if self.rect.colliderect(obj.rect):
                    self.rect.x = oldX
                    self.rect.y = oldY
                    if music_on:
                        touch.play()
            if obj.type == 'bonus' and obj != self:
                if self.rect.colliderect(obj.rect):
                    self.rect.x = oldX
                    self.rect.y = oldY
                    if music_on:
                        bonus_music.play()
                    if obj.bonus_type == 0:
                        self.moveSpeed += 1
                    else:
                        self.health += 1
                    objects.remove(obj)

        # if tanks goes to out of border
        if self.rect.y <= 0 or self.rect.x <= 0 or self.rect.y >= HEIGHT or self.rect.x >= WIDTH:
            self.rect.x = oldX
            self.rect.y = oldY
            if music_on:
                touch.play()

        # delays in shoots
        if keys[self.keyShoot] and self.shotTimer == 0:
            dx = DIRECTS[self.direct][0] * self.bulletSpeed
            dy = DIRECTS[self.direct][1] * self.bulletSpeed
            Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, self.bulletDamage)
            self.shotTimer = self.shotDelay

        if self.shotTimer > 0: self.shotTimer -= 1

    def draw(self):
        window.blit(self.image, self.rect)

    def damage(self, value, music_on):
        self.health -= value
        if self.health <= 0:
            objects.remove(self)
            if music_on:
                fail.play()
            return "game_over"
