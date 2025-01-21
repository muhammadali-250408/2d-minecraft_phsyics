import pygame


class ClicK_Checker():
    def __init__(self, mouse_pos):
        self.x = mouse_pos[0]
        self.y = mouse_pos[1]
        self.checker = pygame.Rect(self.x, self.y, 5,5)



    def draw(self):
        self.checker = pygame.Rect(self.x, self.y, 5,5)
