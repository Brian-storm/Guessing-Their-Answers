"""
Screen size: 1280 x 720
This file records classes of sprites:
-Button (GUI)
-Characters
"""

import pygame
import time
from Resources.colors_and_fonts import BREE_SERIF, LIGHT_GRAY, RED, WHITE, YELLOW


class Button(pygame.sprite.Sprite):
    """Button to be clicked by mouse, or tapped by keyboard"""

    def __init__(self, text: bool | str, button_color: str | int = RED,
                 button_size: tuple[int, int] = (200, 100),
                 *, center_pos: tuple[int, int]):
        super().__init__()
        self.text = text if text else None
        self.button_color = button_color
        self.button_size = button_size
        self.center = center_pos

        self.surf = pygame.Surface(self.button_size)
        self.surf.fill(self.button_color)
        
        self.surf_h = pygame.Surface(self.button_size)
        self.surf_h.fill(self.button_color)
        
        # Creating base surface and hovered animation (suffix: _h)
        if self.text is not None:  # maybe a button without texts but with IMG
            self.text_font = pygame.font.Font(BREE_SERIF, 30) # TODO: may change the font size according to S/M/L settings
            self.text_surf = self.text_font.render(self.text, True, RED, button_color)
            self.text_rect = self.text_surf.get_rect(center=self.center)

            self.text_font_h = pygame.font.Font(BREE_SERIF, 35)  # TODO: may change the font size according to S/M/L settings
            self.text_surf_h = self.text_font_h.render(self.text, True, RED, button_color)
            self.text_rect_h = self.text_surf_h.get_rect(center=self.center)

            self.rect = self.surf.get_rect(center=self.center)
            self.rect_h = self.surf_h.get_rect(center=self.center)

            text_L, text_R = (self.center[0] - self.rect.left, self.center[1]-self.rect.top)
            text_center = (text_L - self.text_rect.width//2, text_R - self.text_rect.height//2)
            text_center_h = (text_L - self.text_rect_h.width//2, text_R - self.text_rect_h.height//2)
            self.surf.blit(self.text_surf, text_center)
            self.surf_h.blit(self.text_surf_h, text_center_h)
        
        self.display, self.display_rect = self.surf.copy(), self.rect.copy()
        
        
    def is_hovered(self, mousePos):
        if self.rect.collidepoint(mousePos):
            self.display, self.display_rect = self.surf_h.copy(), self.rect_h.copy()
            # TODO: some redudant codes here, maybe the rect are the same
        else:
            self.display, self.display_rect = self.surf.copy(), self.rect.copy()
            # TODO: some redudant codes here

    def is_clicked(self, mousePos):
        if self.rect.collidepoint(mousePos):
            self.display.fill(WHITE)

        # button animation to be matched with that of transition scene

class Button_Group(pygame.sprite.Group):
    def __init__(self,):
        pass
    
    def update(self,):
        pass
