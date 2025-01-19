import pygame
import player
import block
import tree
import random
from terrain_gen import make_tile_map


class mainGame():
    def __init__(self, bg_color, width, height, title):
        # SETTING UP VARIABLES
        self.bg_color = bg_color
        self.width = width
        self.height = height
        self.title = title
        self.running = True

        # CLOCK
        self.clock = pygame.time.Clock()
        self.fps = 0

        # SETTING UP PYGAME AND WINDOW
        pygame.init()
        self.window = pygame.display
        self.screen = self.window.set_mode((self.width, self.height))
        self.window.set_caption(self.title)

        # PLAYER
        self.player = player.player(100, 100, 1.5, 0, 3, 1, 9.81, (255, 0, 0))

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
        self.player.handle_keys()

        if not self.player.isOnFloor:
            self.player.isJumping = True

        print(
            f"COLLIDER X: {self.player.collider.x} PLAYER X: {self.player.x}\nCOLLIDER Y: {self.player.collider.y} PLAYER Y: {self.player.y}\n")

        for collider in self.world_colliders:
            if self.player.collider.colliderect(collider):
                print("========================================================")
                self.player.isOnFloor = True
                self.player.isJumping = False
                self.player.y_vel = 0

        # UPDATE TEXT TEXT
        self.x_cords_text = self.mc_font.render(f"X: {round(self.player.x)}", True, (0, 0, 0))
        self.y_cords_text = self.mc_font.render(f"Y: {round(self.player.y)}", True, (0, 0, 0))
        self.fps_text = self.mc_font.render(f"FPS: {self.fps}", True, (0, 0, 0))

    # INPUT HANDLING
    def input_handler(self):
        for event in pygame.event.get():

            # ENDING WINDOW WHEN PRESS X
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self):
        self.screen.fill(self.bg_color)
        self.player.draw(self.screen)
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
        #DISPLAY FPS TEXT
        self.screen.blit(self.fps_text, (0,32))

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
