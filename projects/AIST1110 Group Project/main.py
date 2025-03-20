import pygame
from Resources.colors_and_fonts import BREE_SERIF,LIGHT_GRAY, RED, WHITE
from Sprites import Button
from sys import exit

# Some main screens
# 1. Main Menua Interface
# 2. Game Scene - 
#       During gameplay (Q&A)
#       Winning Celebration Animation
#       Score/Ranking Visualization
# 3. (more...) 


pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.SCALED)
# pygame.RESIZABLE allows window toggling but requires alignment adjustment
# Decide whether to use pygame.RESIZABLE
icon = pygame.image.load(r"Resources\icon\game_icon1.png")
pygame.display.set_icon(icon)

pygame.display.set_caption("Guessing Their Answers")
clock = pygame.time.Clock()

# TODO: Look for resources: background.png, characters.png, ...
title_font = pygame.font.Font(BREE_SERIF, 65)
title_surf = title_font.render('Guessing Their Answers', True, LIGHT_GRAY, RED)
title_rect = title_surf.get_rect(midbottom=(640, 180))

play_button = Button("PLAY", button_color=LIGHT_GRAY, button_size=(250, 115), center_pos=(640, 330))
lang_button = Button("Language", button_color=LIGHT_GRAY, button_size=(250, 115), center_pos= (640, 480))

# button_group = Button_Group()
button_group = pygame.sprite.Group()
button_group.add(play_button, lang_button)

# For background, check Resources (1. sky&clouds 2. ocean&clouds)
...

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            for button in button_group:
                button.is_hovered(mouse_pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in button_group:
                button.is_clicked(mouse_pos)

    # TODO: Create rectangles to place characters and texts
    # e.g. question text field, answer text field, ...
    # OR, draw the required field using pygame.draw

    screen.fill((0, 0, 0))
    screen.blit(title_surf, title_rect)
    screen.blit(play_button.display, play_button.display_rect)
    screen.blit(lang_button.display, lang_button.display_rect)
    for button in button_group:
        button.display, button.display_rect = button.surf.copy(), button.rect.copy()
        # TODO: some redudant codes here
    pygame.display.flip()
    clock.tick(30)
