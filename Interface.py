import pygame

from GameObject import GameObject, objects, window, imageHealths, WIDTH, HEIGHT, imageFlashes


class Interface(GameObject):
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        font = pygame.font.Font(None, 30)
        i = 0
        for obj in objects:
            if obj.type == 'tank':
                window.blit(imageHealths[obj.order - 1], pygame.Rect(5 + i * 70, 5, 24, 24))
                window.blit(imageFlashes[obj.order - 1], pygame.Rect(5 + (i + 2) * 75, 5, 24, 24))

                text1 = font.render(str(obj.moveSpeed), 1, obj.color)
                text = font.render(str(obj.health), 1, obj.color)
                rect = text.get_rect(center=(5 + i * 70 + 32, 5 + 11))
                window.blit(text, rect)
                rect1 = text1.get_rect(center=(5 + (i + 2) * 75 + 32, 5 + 11))
                window.blit(text1, rect1)
                i += 1

    @staticmethod
    def draw_start_menu():
        window.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 40)
        title = font.render('My Game', True, (255, 255, 255))
        start_button = font.render('(Any Key) - Start ', True, (255, 255, 255))
        music_button = font.render('M - Music (On/Off)', True, (255, 255, 255))
        pause_button = font.render('BCKSPC - Pause', True, (255, 255, 255))
        window.blit(title, (WIDTH / 2 - title.get_width() / 2, HEIGHT / 2 - title.get_height() / 2))
        window.blit(start_button,
                    (WIDTH / 2 - start_button.get_width() / 2, HEIGHT / 2 + start_button.get_height() / 2))
        window.blit(music_button,
                    (WIDTH / 2 - music_button.get_width() / 2,
                     HEIGHT / 2 + start_button.get_height() + music_button.get_height() / 2))
        window.blit(pause_button,
                    (WIDTH / 2 - pause_button.get_width() / 2,
                     HEIGHT / 2 + start_button.get_height() + music_button.get_height() + pause_button.get_height() / 2))
        pygame.display.update()

    @staticmethod
    def draw_restart_menu():
        window.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 40)
        title = font.render('My Game', True, (255, 255, 255))
        start_button = font.render('ESC - Unpause', True, (255, 255, 255))
        music_button = font.render('M - Music (On/Off)', True, (255, 255, 255))
        window.blit(title, (WIDTH / 2 - title.get_width() / 2, HEIGHT / 2 - title.get_height() / 2))
        window.blit(start_button,
                    (WIDTH / 2 - start_button.get_width() / 2, HEIGHT / 2 + start_button.get_height() / 2))
        window.blit(music_button,
                    (WIDTH / 2 - music_button.get_width() / 2,
                     HEIGHT / 2 + start_button.get_height() + music_button.get_height() / 2))
        pygame.display.update()

    @staticmethod
    def draw_game_over_screen():
        window.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 40)
        title = font.render('Game Over', True, (255, 255, 255))
        quit_button = font.render('Q - Quit', True, (255, 255, 255))
        window.blit(title, (WIDTH / 2 - title.get_width() / 2, HEIGHT / 2 - title.get_height() / 3))
        window.blit(quit_button,
                    (WIDTH / 2 - quit_button.get_width() / 2, HEIGHT / 2 + quit_button.get_height() / 2))
        pygame.display.update()