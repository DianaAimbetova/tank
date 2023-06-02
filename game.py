import random
import sys

import pygame
from pygame import KEYDOWN

from Block import draw_random_block
from GameObject import objects, window, bullets, clock, FPS, game_state, music_on, WIDTH, HEIGHT, X_PIXEL, Y_PIXEL, \
    imageBackgrounds
from Interface import Interface
from Bonus import draw_random_stars
from Tank import Tank


def build_tanks():
    x1, y1 = random.randint(1, WIDTH / 2), random.randint(1, HEIGHT / 2)
    x2, y2 = random.randint(1, WIDTH / 2), random.randint(1, HEIGHT / 2)
    rect1 = pygame.Rect(x1, y1, X_PIXEL, Y_PIXEL)
    rect2 = pygame.Rect(x2, y2, X_PIXEL, Y_PIXEL)
    while rect1.colliderect(rect2):
        x2, y2 = random.randint(1, WIDTH), random.randint(1, HEIGHT)
        rect1 = pygame.Rect(x1, y1, X_PIXEL, Y_PIXEL)
        rect2 = pygame.Rect(x2, y2, X_PIXEL, Y_PIXEL)
    Tank('blue', x1, y1, 0, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE), 1)
    Tank('green', x2, y2, 0, (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_RETURN), 2)


build_tanks()
interface = Interface()

draw_random_block()
draw_random_stars()

game_over = False
bg = imageBackgrounds[random.randint(0, 2)]
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if game_state == "start_menu":
        Interface.draw_start_menu()
        key_down_event_list = pygame.event.get(KEYDOWN)
        general_event_list = pygame.event.get()
        if len(key_down_event_list) != 0:
            game_state = "game"
            game_over = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_m]:
                if music_on:
                    music_on = False
                    pygame.mixer_music.stop()
                else:
                    music_on = True
                    pygame.mixer_music.play()
    elif game_state == "game_over":
        Interface.draw_game_over_screen()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game_state = "start_menu"
        if keys[pygame.K_q]:
            pygame.quit()
            sys.exit()
    elif game_state == "game":
        keys = pygame.key.get_pressed()

        for bullet in bullets:
            state = bullet.update(music_on)
            if state == 'game_over':
                game_state = state

        for obj in objects:
            if obj.type == 'tank' or obj.type == 'bullet':
                obj.update(keys, music_on)
            else:
                obj.update()

        interface.update()

        window.fill('black')
        bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
        window.blit(bg, pygame.Rect(0, 0, WIDTH, HEIGHT))
        for obj in objects:
            if obj.type != 'block':
                obj.draw()
            else:
                obj.draw(obj.level)
        for bullet in bullets:
            bullet.draw()

        interface.draw()
        if keys[pygame.K_BACKSPACE]:
            game_state = 'pause'
        pygame.display.update()
        clock.tick(FPS)
    elif game_state == 'pause':
        Interface.draw_restart_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_m]:
            if music_on:
                music_on = False
                pygame.mixer_music.stop()
            else:
                music_on = True
                pygame.mixer_music.play()
        if keys[pygame.K_ESCAPE]:
            game_state = 'game'
    elif game_over:
        game_state = "game_over"
        game_over = False
