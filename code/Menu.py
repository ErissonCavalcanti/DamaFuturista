#!/usr/bin/python

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, C_WHITE


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load("./asset/Menu.mp3")
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, text="Dama", text_color=(COLOR_ORANGE), text_center_pos=((WIN_WIDTH / 2), 70))
            self.menu_text(50, text="Futurista", text_color=(COLOR_ORANGE), text_center_pos=((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], C_WHITE, text_center_pos=((WIN_WIDTH / 2), 200 + 30 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # End game

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):

        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

        if text_color == C_WHITE:
            padding = 10  # espaço extra ao redor do texto
            bg_rect = Rect(
                text_rect.left - padding,
                text_rect.top - padding,
                text_rect.width + 2 * padding,
                text_rect.height + 2 * padding
            )
            roxo = (128, 0, 128)  # cor roxa (RGB)
            pygame.draw.rect(self.window, roxo, bg_rect, border_radius=5)

        self.window.blit(source=text_surf, dest=text_rect)
        

