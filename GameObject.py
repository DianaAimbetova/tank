import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
X_PIXEL = 75
Y_PIXEL = 70

X_PIXEL_BLOCK = 44
Y_PIXEL_BLOCK = 62

X_PIXEL_BULLET = 12
Y_PIXEL_BULLET = 26

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Tanks')

imageBlocks = [pygame.image.load('PNG/Obstacles/barrelGrey_side.png'),
               pygame.image.load('PNG/Obstacles/barrelRed_side.png')]
imageTanks = [pygame.image.load('PNG/Tanks/tankBlue.png'),
              pygame.image.load('PNG/Tanks/tankGreen.png')]
imageBangs = [pygame.image.load('PNG/Smoke/smokeGrey0.png'),
              pygame.image.load('PNG/Smoke/smokeOrange0.png'),
              pygame.image.load('PNG/Smoke/smokeWhite0.png')]

imageBullets = [pygame.image.load('PNG/Bullets/bulletBlue.png'),
                pygame.image.load('PNG/Bullets/bulletGreen.png')]

imageHealths = [pygame.image.load('PNG/health/blue-heart.png'),
                pygame.image.load('PNG/health/green-heart.png')]

imageFlashes = [pygame.image.load('PNG/health/blue-flash.png'),
                pygame.image.load('PNG/health/green-flash.png')]

imageBackgrounds = [pygame.image.load('PNG/Environment/sand.png'),
                    pygame.image.load('PNG/Environment/grass.png'),
                    pygame.image.load('PNG/Environment/dirt.png')]

imageBonuses = [pygame.image.load('PNG/Bonus/star.png'),
                pygame.image.load('PNG/Bonus/heart.png')]

programIcon = pygame.image.load('PNG/Icon/icon.ico')

pygame.display.set_icon(programIcon)

pygame.mixer.music.load('Sounds/fon.mp3')
pygame.mixer.music.play()

shout = pygame.mixer.Sound('Sounds/Shot.wav')
touch = pygame.mixer.Sound('Sounds/Touch.wav')
fail = pygame.mixer.Sound('Sounds/fail.mp3')
bonus_music = pygame.mixer.Sound('Sounds/bonus.wav')

DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0]]

game_state = "start_menu"
music_on = True
objects = []
bullets = []
global rect


class GameObject:
    def update(self, **kwargs):
        pass

    def draw(self, **kwargs):
        pass
