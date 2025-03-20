import pygame
from sys import exit

# Some aesthetic colors
Blue = (55, 107, 137)
Red = (128, 25, 34)
Yellow = (236, 178, 67)
Light_Gray = (178, 181, 190)
Dark_Gray = (67, 70, 81)

pygame.init()
screen = pygame.display.set_mode((1280, 720))
# pygame.RESIZABLE allows window toggling but requires alignment adjustment
# Decide whether to use pygame.RESIZABLE

pygame.display.set_caption("Guessing Their Answers")
clock = pygame.time.Clock()

#TODO: Look for resources: background.png, characters.png, ...
title_font = pygame.font.Font(r"Resources\font\Bree_Serif\BreeSerif-Regular.ttf", 40)
title_surf = title_font.render('Guessing Their Answers', True, Light_Gray, Red)
title_rect = title_surf.get_rect(midbottom = (640, 200))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos
    
    #TODO: Create rectangles to place characters and texts
    #e.g. question text field, answer text field, ...
    #OR, draw the required field using pygame.draw
    
    screen.blit(title_surf, title_rect)

    pygame.display.update()
    clock.tick(60)