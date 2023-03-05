import pygame

from .themes import day_theme
from .functions import load_image
from .intention import Intent




SIZE = WIDTH, HEIGHT = 300, 300
FPS = 60
clock = pygame.time.Clock()

display = None
from .themes import *


def init(screen_size=SIZE, fps=60):
    global SIZE, FPS, display
    SIZE = screen_size
    FPS = fps
    pygame.init()
    display = pygame.display.set_mode(SIZE)


def run(start_screen, theme=day_theme):
    intent = Intent()
    cur_screen = start_screen(display, intent, Theme(theme.data))

    running = True
    while running:
        if intent.has_intention:
            cur_screen = intent.get_screen(display)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                cur_screen._push_event(event)
        display.fill((0, 0, 0))
        cur_screen._draw(clock.tick(FPS))
        pygame.display.flip()

SCROLL_SHIFT = 25

pygame.display.set_caption("UIPL program")
BACKTOGAMESCREEN = pygame.USEREVENT + 1
