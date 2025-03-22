"""
Screen size: 1280 x 720
This file records classes of sprites:
- Button
- Button_Group
- Q_and_A (upcoming)
"""

import pygame
from Resources.colors_and_fonts import BREE_SERIF, LIGHT_GRAY, RED, YELLOW


class Button(pygame.sprite.Sprite):
    """Button to be interacted by mouse"""

    def __init__(self, text: bool | str = None, button_color: str | int = LIGHT_GRAY,
                 button_size: tuple[int, int] = (220, 100),
                 *, center_pos: tuple[int, int]):
        super().__init__()
        width, height = button_size
        self.text = text if text else None
        self.button_color = button_color
        self.button_size = (width, height)
        self.center = center_pos

        # self.norm is the original appearance of the buttons
        self.norm = pygame.Surface(self.button_size, pygame.SRCALPHA)
        self.norm.fill(self.button_color)
        self.rectA = self.norm.get_rect(center=self.center)

        # for is_clicked
        self.is_clicked = False
        self.countdown = 0
        self.clicked = self.norm.copy()

        # Creating text surface and blit to self.norm
        if self.text is not None:
            self.text_font = pygame.font.Font(BREE_SERIF, 45)
            self.text_surf = self.text_font.render(self.text, True, RED, button_color)
            self.text_surf_clicked = self.text_font.render(self.text, True, YELLOW, button_color)
            self.text_rect = self.text_surf.get_rect(center=self.center)

            text_L, text_R = (self.center[0] - self.rectA.left, self.center[1]-self.rectA.top)
            text_center = (text_L - self.text_rect.width//2, text_R - self.text_rect.height//2)

            self.norm.blit(self.text_surf, text_center)
            self.clicked.blit(self.text_surf_clicked, text_center)

        # TODO: maybe a button without texts but with IMG

        # Creating hovered appearances
        self.hovered = pygame.transform.rotozoom(self.norm, 6, 1.2)
        self.clicked = pygame.transform.rotozoom(self.clicked, 6, 1.2)
        self.rectB = self.hovered.get_rect(center=self.center)

        # self.image and self.rect are for display (by Group.draw())
        # AND CANNOT CHANGE THE NAMES (due to inheritance)
        self.image = self.norm.copy()
        self.rect = self.rectA

    def check_hovered(self, mousePos):
        if self.rectA.collidepoint(mousePos):
            self.image = self.hovered.copy()
            self.rect = self.rectB
        else:
            self.image = self.norm.copy()
            self.rect = self.rectA

    def check_clicked(self, mousePos):
        if self.rectA.collidepoint(mousePos):
            self.image = self.clicked.copy()
            self.rect = self.rectB
        else:
            self.check_hovered(mousePos)

        # The white fill covers the entire rect,
        # which is bad. Optimization needed here
        # also, for transisiton scene (not yet made), 
        # button animation should be matched


class Button_Group(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def update(self, mousePos, clicked):
        for button in self.sprites():
            if clicked:
                button.is_clicked = True
                button.countdown = pygame.time.get_ticks() + 100
                button.check_clicked(mousePos)
            elif pygame.time.get_ticks() >= button.countdown:
                button.is_clicked = False
                button.countdown = 0
                button.check_hovered(mousePos)

    # def set_to_normal(self):
    #     for button in self.sprites():
    #         button.image = button.norm.copy()
    #         button.rect = button.norm_rect.copy()


# Implement Q&A mechanic with ChatGPT here
# Utitlize "chatgpt.py"

# class Q_and_A():
#     def __init__():
#         pass

# class Question(Q_and_A):
#     def __init__(self, Ques_text, field_size, field_color, center_pos):
#         pass

