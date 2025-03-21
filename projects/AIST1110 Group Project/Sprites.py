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
        width, height = button_size
        self.text = text if text else None
        self.button_color = button_color
        self.button_size = (width, height)
        self.center = center_pos
        self.hovered = False

        self.surf = pygame.Surface(self.button_size)
        self.surf.fill(self.button_color)

        # Creating text surface and blit to button
        # TODO: may change the font size according to S/M/L settings
        if self.text is not None:
            self.text_font = pygame.font.Font(BREE_SERIF, 40)
            self.text_surf = self.text_font.render(self.text, True, RED, button_color)
            self.text_rect = self.text_surf.get_rect(center=self.center)

            self.rect = self.surf.get_rect(center=self.center)

            text_L, text_R = (self.center[0] - self.rect.left, self.center[1]-self.rect.top)
            text_center = (text_L - self.text_rect.width//2, text_R - self.text_rect.height//2)
            self.surf.blit(self.text_surf, text_center)

        # TODO: maybe a button without texts but with IMG

        self.hover_surf = pygame.transform.rotozoom(self.surf, 6, 1.2)
        self.hover_rect = self.hover_surf.get_rect(center=self.center)

        self.display_surf = self.surf.copy()
        self.display_rect = self.rect.copy()

    def is_hovered(self, mousePos):
        if self.rect.collidepoint(mousePos):
            self.display_surf = self.hover_surf.copy()
            self.display_rect = self.hover_rect.copy()

    def is_clicked(self, mousePos):
        if self.rect.collidepoint(mousePos):
            self.display_surf.fill(WHITE)
            pygame.time.delay(50)
        # button shines when clicked, but the animation is not good,
        # as the rect covers extra area due to the rotozoomed surf,
        # so more optimization are needed here
        
        # also, for transisiton scene, 
        # button animation should be matched


class Button_Group(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def update(self, mousePos, event_type):
        for button in self.sprites():
            if event_type == pygame.MOUSEMOTION:
                button.is_hovered(mousePos)
            if event_type == pygame.MOUSEBUTTONDOWN:
                button.is_clicked(mousePos)

    def return_to_normal(self):
        for button in self.sprites():
            button.display_surf = button.surf.copy()
            button.display_rect = button.rect.copy()

    def display_button(self, screen):
        for button in self.sprites():
            screen.blit(button.display_surf, button.display_rect)
