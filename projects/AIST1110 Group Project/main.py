import pygame
from Resources.colors_and_fonts import BREE_SERIF,LIGHT_GRAY, RED, WHITE
from Sprites import Button, Button_Group
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
title_rect = title_surf.get_rect(midbottom=(640, 160))

play_button = Button("PLAY", button_color=LIGHT_GRAY, button_size=(220, 100), center_pos=(640, 260))
lang_button = Button("Language", button_color=LIGHT_GRAY, button_size=(220, 100), center_pos= (640, 390))
diff_button = Button("Difficulty", button_color=LIGHT_GRAY, button_size=(220, 100), center_pos=(640, 520))

button_group = Button_Group()
button_group.add(play_button, lang_button, diff_button)

# For background, check Resources (1. sky&clouds 2. ocean&clouds)
...

running = True
while running:
    mousePos = pygame.mouse.get_pos()
    button_group.update(mousePos, pygame.MOUSEMOTION)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            button_group.update(mousePos, event.type)


    # TODO: Create rectangles to place characters and texts
    # e.g. question text field, answer text field, ...
    # OR, draw the required field using pygame.draw

    screen.fill((0, 0, 0))
    screen.blit(title_surf, title_rect)
    button_group.display_button(screen)
    button_group.return_to_normal()
        # TODO: some redudant codes here
    pygame.display.flip()
    clock.tick(30)
