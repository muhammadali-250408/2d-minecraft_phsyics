import pygame

class Block():
    def __init__(self, block_type, x, y):
        self.x = x
        self.y = y
        self.block_type = block_type

        if block_type == "Grass":
            self.texture = pygame.image.load("Assets/Blocks/Grass.png")
        elif block_type == "Wood":
            self.texture = pygame.image.load("Assets/Blocks/Oak_log.png")
        elif block_type == "Leave":
            self.texture = pygame.image.load("Assets/Blocks/leave.png")
        elif block_type == "Dirt":
            self.texture = pygame.image.load("Assets/Blocks/dirt.png")

    def draw(self, screen):
        screen.blit(self.texture,(self.x, self.y))