import pygame

from UserInterfafce.intention import Intent
from UserInterfafce import display


class Screen(pygame.Surface):
    def __init__(self, display, intent, theme):
        super(Screen, self).__init__(display.get_size(), pygame.SRCALPHA, 32)
        self.__display = display
        self.__intent = intent
        self.__theme = theme
        self.__theme_src = theme
        self.__elements = list()

    def get_theme(self):
        return self.__theme

    def set_theme(self, theme):
        self.__theme.data = theme.data

    def _draw(self, tick):
        self.fill((0, 0, 0, 0))
        self.blit(self.__theme.data["background"], (0, 0))
        for element in self.__elements:
            element._draw(tick)
        self.__display.blit(self, (0, 0))

    def _push_event(self, event):
        self.event_process(event)
        for element in self.__elements[::-1]:
            if element._push_event(event):
                return True

    def event_process(self, event):
        pass

    def add_element(self, element):
        self.__elements.append(element)

    def set_intent(self, intent: Intent):
        self.__intent = intent

    def get_mouse_pos(self):
        if self.__display == display:
            return pygame.mouse.get_pos()
        return self.__display.get_mouse_pos()
