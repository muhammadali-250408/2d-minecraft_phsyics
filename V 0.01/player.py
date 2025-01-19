import pygame


class player():
    def __init__(self, x, y, x_vel, y_vel, max_vel, acc, grav, color):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.max_vel = max_vel
        self.acc = acc
        self.grav = grav

        self.height = 10
        self.width = 5

        self.isJumping = False
        self.isOnFloor = False

        self.color = color

        self.collider = pygame.Rect(self.x, self.y, self.width, self.height)

    def handle_keys(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            if self.x_vel <= self.max_vel:
                self.x_vel += (self.acc / (60 * 60))
            self.x += self.x_vel / 30
            self.collider.x += self.x_vel / 30

        print((self.acc / (60 * 60)))

        if keys[pygame.K_a]:
            if self.x_vel <= self.max_vel:
                self.x_vel += (self.acc / (60 * 60))
            self.x -= self.x_vel / 30
            self.collider.x -= self.x_vel / 30

        if keys[pygame.K_SPACE]:
            if self.isOnFloor:
                self.y_vel = 2.5
                self.isJumping = True
                self.isOnFloor = False

        if self.isJumping:
            print("sigma")
            if self.isOnFloor:
                self.y_vel = 0
                self.isJumping = False
            else:
                self.y_vel -= self.grav / (60 * 60)  # CONVERTING METERS PER SECOND INTO METERS FRAME
                self.y -= self.y_vel / 30
                self.collider.y -= self.y_vel / 30
                print(f"Y VELOCITY: {self.y_vel}")

            print(self.x_vel)
            print(self.x)
            print("\n\n")

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        self.collider = pygame.Rect(self.x, self.y, self.width, self.height)
