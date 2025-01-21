import random
import block
import pygame


class tree():
    def __init__(self, x, y):
        self.height = random.randint(3, 5)
        self.x = x
        self.y = y

        self.tree_arr = []
        self.leave_arr = []
        self.texture = self.texture = pygame.image.load("Assets/Blocks/Oak_log.png")
        self.leave_texture = pygame.image.load("Assets/Blocks/leave.png")

    def make_tree_arr(self):
        for i in range(self.height):
            self.tree_arr.append(block.Block(block_type="Wood", x=self.x, y=(self.y-(i*16))))
        for i in range(3):
            for x in range(2):

                self.leave_arr.append(block.Block(block_type="Leave", x=(self.x+((i-1)*16)), y=(self.y - (self.height * 16)) - (x * 16)))

    def draw(self, screen):
        screen.blit(self.texture,(self.x, self.y))
