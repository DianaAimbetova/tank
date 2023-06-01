import pygame
from random import randint

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
X_PIXEL = 75
Y_PIXEL = 70

X_PIXEL_BLOCK = 44
Y_PIXEL_BLOCK = 62

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Tanks')

imageBlock = pygame.image.load('PNG/Obstacles/barrelRed_side.png')
imageTanks = [pygame.image.load('PNG/Tanks/tankBlue.png'),
              pygame.image.load('PNG/Tanks/tankGreen.png')]
imageBangs = [pygame.image.load('PNG/Smoke/smokeGrey0.png'),
              pygame.image.load('PNG/Smoke/smokeOrange0.png'),
              pygame.image.load('PNG/Smoke/smokeWhite0.png')]

pygame.mixer.music.load('Sounds/fon.mp3')
pygame.mixer.music.play()

shout = pygame.mixer.Sound('Sounds/Shot.wav')
touch = pygame.mixer.Sound('Sounds/Touch.wav')
fail = pygame.mixer.Sound('Sounds/fail.mp3')

DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0]]


class Tank:
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

    def update(self):
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
                    touch.play()

        # if tanks goes to out of border
        if self.rect.y <= 0 or self.rect.x <= 0 or self.rect.y >= HEIGHT - rect.size[0] or self.rect.x >= WIDTH - \
                rect.size[1]:
            self.rect.x = oldX
            self.rect.y = oldY
            touch.play()

        # delays in shoots
        if keys[self.keyShoot] and self.shotTimer == 0:
            dx = DIRECTS[self.direct][0] * self.bulletSpeed
            dy = DIRECTS[self.direct][1] * self.bulletSpeed
            Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, self.bulletDamage)
            self.shotTimer = self.shotDelay

        if self.shotTimer > 0: self.shotTimer -= 1

    def draw(self):
        # draw tank
        window.blit(self.image, self.rect)
        # pygame.draw.rect(window, self.color, self.rect)

        # draw muzzle
        # x = self.rect.centerx + DIRECTS[self.direct][0] * 50
        # y = self.rect.centery + DIRECTS[self.direct][1] * 50
        # pygame.draw.line(window, 'white', self.rect.center, (x, y), 4)

    def damage(self, value):
        self.health -= value
        if self.health <= 0:
            objects.remove(self)
            print(self.color, self.type, 'dead')
            fail.play()


class Bullet:
    def __init__(self, parent, px, py, dx, dy, damage):
        bullets.append(self)
        self.px = px
        self.py = py
        self.dx = dx
        self.dy = dy
        self.damage = damage
        self.parent = parent

    def update(self):
        self.px += self.dx
        self.py += self.dy

        # if bullet is out of window
        if self.px < 0 or self.px > WIDTH or self.py < 0 or self.py > HEIGHT:
            bullets.remove(self)
        else:
            for obj in objects:
                # if bullet hits the object and its not the same object where bullet starts
                if obj != self.parent and obj.rect.collidepoint(self.px, self.py):
                    obj.damage(self.damage)
                    bullets.remove(self)
                    Smoke(self.px, self.py)
                    shout.play()
                    break

    def draw(self):
        pygame.draw.circle(window, 'yellow', (self.px, self.py), 2)


class Block:
    def __init__(self, px, py, sizeX, sizeY):
        objects.append(self)
        self.type = 'block'

        self.rect = pygame.Rect(px, py, sizeX, sizeY)
        self.health = 1

    def update(self):
        pass

    def draw(self):
        window.blit(imageBlock, self.rect)
        # pygame.draw.rect(window, 'green', self.rect)
        # pygame.draw.rect(window, 'gray20', self.rect, 2)

    def damage(self, value):
        self.health -= 1
        if self.health <= 0:
            objects.remove(self)


class Interface:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        font = pygame.font.Font(None, 30)
        i = 0
        for obj in objects:
            if obj.type == 'tank':
                pygame.draw.rect(window, obj.color, pygame.Rect(5 + i * 70, 5, 25, 25))
                text = font.render(str(obj.health), 1, obj.color)
                rect = text.get_rect(center=(5 + i * 70 + 32, 5 + 11))
                window.blit(text, rect)
                i += 1


class Smoke:
    def __init__(self, x, y):
        objects.append(self)
        self.x = x
        self.y = y
        self.type = 'smoke'
        self.frame = 0

    def update(self):
        self.frame += 0.2
        if self.frame >= 3:
            objects.remove(self)

    def draw(self):
        image = imageBangs[int(self.frame)]
        rect = image.get_rect(center = (self.x, self.y))
        window.blit(image, rect)


bullets = []
objects = []

Tank('blue', 100, 275, 0, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE), 1)
Tank('green', 650, 275, 0, (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_DELETE), 2)
interface = Interface()

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
    Block(x, y, X_PIXEL_BLOCK, Y_PIXEL_BLOCK)

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()

    for bullet in bullets:
        bullet.update()

    for obj in objects:
        obj.update()

    interface.update()

    window.fill('black')
    for obj in objects:
        obj.draw()
    for bullet in bullets:
        bullet.draw()

    interface.draw()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
