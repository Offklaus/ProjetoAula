#!/usr/bin/python
#-*- coding: utf-8 -*-
from pygame import Rect, Surface, font
import pygame.image

from const import WIN_WIDTH


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('./assets/menu_bg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", (255, 128, 0),(WIN_WIDTH / 2), 70)
            pygame.display.flip()

    def menu_text(self,text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: font = pygame.font.SysFont(name="Lacida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color) 
        text_rect: Rect = text.surf.get_rect(center= text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)              

    