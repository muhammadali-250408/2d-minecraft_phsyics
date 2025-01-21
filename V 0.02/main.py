import pygame
import player
import block
import tree
import random
import click_checker
from terrain_gen import make_tile_map
import threading


class mainGame():
    def __init__(self, bg_color, width, height, title):
        # SETTING UP VARIABLES
        self.hovered_block_index = 0
        self.update_thread = None
        self.draw_thread = None
        self.bg_color = bg_color
        self.width = width
        self.height = height
        self.title = title
        self.running = True
        self.is_over_block = False
        self.is_player_colliding = False

        # CLOCK
        self.clock = pygame.time.Clock()
        self.fps = 0

        # SETTING UP PYGAME AND WINDOW
        pygame.init()
        self.window = pygame.display
        self.screen = self.window.set_mode((self.width, self.height))
        self.window.set_caption(self.title)

        # PLAYER
        self.player = player.player(100, 100, 10, 0, 10, 1, 9.81, (255, 0, 0))

        self.click_checker = click_checker.ClicK_Checker(pygame.mouse.get_pos())

        # === TERRAIN GENERATION
        # WORLD GEN
        self.world = []
        self.world_colliders = []

        # MAKE THE WORLD
        tile_map = make_tile_map("map.txt")
        for i in range(24):
            for a in range(50):
                print(f"i: {i}\nA {a}")
                if tile_map[i][a] == "1":
                    self.world.append(block.Block("Grass", (16 * (a - 1)), (16 * (i - 1))))
                    self.world_colliders.append(pygame.Rect((16 * (a - 1)), (16 * (i - 1)), 16, 16))
                elif tile_map[i][a] == "2":
                    self.world.append(block.Block("Dirt", (16 * (a - 1)), (16 * (i - 1))))
                    self.world_colliders.append(pygame.Rect((16 * (a - 1)), (16 * (i - 1)), 16, 16))
                else:
                    pass

        # TREE GENERATION
        self.trees_data_arr = []
        self.tree_leaves_data_arr = []
        for i in range(17):
            self.tree_data = tree.tree(random.randint(0, 800), 168)
            self.tree_data.make_tree_arr()
            self.tree_data_arr = self.tree_data.tree_arr
            self.tree_leave_data = self.tree_data.leave_arr

            self.trees_data_arr.append(self.tree_data_arr)
            self.tree_leaves_data_arr.append(self.tree_leave_data)
            print(f"========================================================{self.tree_data_arr}")

        # === TEXT DISPLAYING MANAGER
        self.mc_font = pygame.font.Font("Assets/Fonts/MCFONT.ttf", 16)
        # X, Y CORDS
        self.x_cords_text = self.mc_font.render(f"X: {self.player.x}", True, (0, 0, 0))
        self.y_cords_text = self.mc_font.render(f"Y: {self.player.y}", True, (0, 0, 0))

        # FPS
        self.fps_text = self.mc_font.render(f"FPS: {self.fps}", True, (0, 0, 0))

    # WHERE PHYSICS AND COLLISION CALCULATION GO
    def update(self):
        # USED TO UPDATE WHERE THE CLICK CHECKER LOCATION IS
        self.click_checker = click_checker.ClicK_Checker(pygame.mouse.get_pos())

        self.player.handle_keys()
        print(f"MOUSE POS: {pygame.mouse.get_pos()[0]}")



        if not self.player.isOnFloor:
            self.player.isJumping = True

        print(
            f"COLLIDER X: {self.player.collider.x} PLAYER X: {self.player.x}\nCOLLIDER Y: {self.player.collider.y} PLAYER Y: {self.player.y}\n")

        self.player.isOnFloor = False
        for collider in self.world_colliders:
            if self.player.collider.colliderect(collider):
                print("========================================================")
                self.player.isOnFloor = True
                self.player.isJumping = False
                self.player.y_vel = 0
                break


        # UPDATE TEXT TEXT
        self.x_cords_text = self.mc_font.render(f"X: {round(self.player.x)}", True, (0, 0, 0))
        self.y_cords_text = self.mc_font.render(f"Y: {round(self.player.y)}", True, (0, 0, 0))
        self.fps_text = self.mc_font.render(f"FPS: {self.fps}", True, (0, 0, 0))

        # === DESTROYING BLOCKS ========================================================================================
        # Checking if mouse is over a block
        self.is_over_block = False
        for blocks in self.world_colliders:
            if self.click_checker.checker.colliderect(blocks):
                print(
                    "HOVER OVERHOVER OVERHOVER OVERHOVER OVERHOVER OVERHOVER OVERHOVER OVERHOVER OVERHOVER OVERHOVER OVERHOVER OVERHOVER OVERHOVER OVERHOVER OVER")
                self.is_over_block = True
                print(f"IS OVER BLOCK = {self.is_over_block}")
                self.hovered_block_index = self.world_colliders.index(blocks)
                break



        print(f"IS OVER BLOCK = {self.is_over_block}")
        # Breaking the block
        if pygame.mouse.get_pressed(num_buttons=3) == (1, 0, 0) and self.is_over_block == True:
            print(
                "CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK ")
            self.world_colliders.pop(self.hovered_block_index)
            self.world.pop(self.hovered_block_index)

    # INPUT HANDLING
    def input_handler(self):
        for event in pygame.event.get():

            # ENDING WINDOW WHEN PRESS X
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self):
        self.screen.fill(self.bg_color)

        for i in range(len(self.world)):
            self.world[i].draw(self.screen)

        for x in range(len(self.trees_data_arr)):
            for i in range(len(self.trees_data_arr[x])):
                self.trees_data_arr[x][i].draw(self.screen)

        for x in range(len(self.tree_leaves_data_arr)):
            for i in range(len(self.tree_leaves_data_arr[x])):
                self.tree_leaves_data_arr[x][i].draw(self.screen)

        # display CORD TEXT
        self.screen.blit(self.x_cords_text, (0, 0))
        self.screen.blit(self.y_cords_text, (0, 16))
        # DISPLAY FPS TEXT
        self.screen.blit(self.fps_text, (0, 32))

        self.player.draw(self.screen)
        self.click_checker.draw()

    def run(self):
        while self.running:
            self.input_handler()
            self.update()
            self.draw()
            self.window.update()
            self.clock.tick()
            self.fps = round(self.clock.get_fps())

        pygame.quit()


if __name__ == "__main__":
    WIDTH, HEIGHT = 800, 400
    BG_COLOR = (135, 206, 235)
    TITLE = "Physics Simulation"

    game = mainGame(BG_COLOR, WIDTH, HEIGHT, TITLE)

    game.run()
