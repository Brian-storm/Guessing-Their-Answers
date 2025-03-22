import pygame
from load_background import load_background
from Resources.colors_and_fonts import BREE_SERIF,LIGHT_GRAY, RED
from Sprites import Button, Button_Group
from sys import exit

# Some main screens
# 1. Main Menual Interface
# 2. Game Scene - 
#       During gameplay (Q&A)
#       Winning Celebration Animation
#       Score/Ranking Visualization
# 3. (more...)


pygame.init()
# pygame.RESIZABLE allows window toggling but requires alignment adjustment
# Decide whether to use pygame.RESIZABLE
screen0 = pygame.display.set_mode((1280, 720), pygame.SCALED)
icon = pygame.image.load(r"Resources\icon\game_icon1.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Guessing Their Answers")
clock = pygame.time.Clock()

# TODO: Look for resources: background.png, characters.png, ...
title_font = pygame.font.Font(BREE_SERIF, 65)
title_surf = title_font.render("Guessing Their Answers", True, LIGHT_GRAY, RED)
title_rect = title_surf.get_rect(midbottom=(640, 160))

play_button = Button("PLAY", center_pos=(640, 260))
lang_button = Button("Language", center_pos= (640, 390))
diff_button = Button("Difficulty", center_pos=(640, 520))

button_group = Button_Group()
button_group.add(play_button, lang_button, diff_button)

# For background, check Resources (1. sky&clouds 2. ocean&clouds)
CloudFileBG = {0: "Morning", 1: "Evening", 2: "Night1", 3: "Night2"}
cloud_filepath = r"Resources\background\Cloud-and-Sky-craftpix-net-995711"
index = lambda: pygame.time.get_ticks() // 4000 % 4

# Main Game Loop
if __name__ == "__main__":
    running = True
    while running:
        mousePos = pygame.mouse.get_pos()
        clicked = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
        
        # Updating the output window
        screen = load_background(screen0, cloud_filepath, CloudFileBG[index()])
        screen.blit(title_surf, title_rect)
        
        button_group.update(mousePos, clicked)
        button_group.draw(screen)

        pygame.display.flip()
        clock.tick(60)