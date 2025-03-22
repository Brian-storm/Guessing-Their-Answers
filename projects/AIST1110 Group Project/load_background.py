import pygame
from pathlib import Path

def load_background(screen, folderPath, folderName):
    filePath_ = Path(folderPath)
    for elem in filePath_.iterdir():
        if elem.name == folderName and elem.is_dir():
            screen_width, screen_height = screen.get_size()
            for pic in elem.iterdir():
                loaded = pygame.image.load(str(pic)).convert_alpha()
                scaled_loaded = pygame.transform.scale(loaded, (screen_width, screen_height))
                screen.blit(scaled_loaded, (0, 0))
    return screen