import pygame
from sys import exit

pygame.init()
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h
screen = pygame.display.set_mode((1280, 720))
# pygame.RESIZABLE allows window toggling but requires alignment adjustment
# Decide whether to use pygame.RESIZABLE

pygame.display.set_caption("Guessing Their Answers")
clock = pygame.time.Clock()
title_font = pygame.font.Font(r"Resources\font\Bree_Serif\BreeSerif-Regular.ttf", 40)

#TODO: background.png, characters, ...
title_surf = title_font.render('Guessing Their Answerss', False, 'Grey')


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
    
    screen.blit(title_surf, (300, 300))

    pygame.display.update()
    clock.tick(60)