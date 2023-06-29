import pygame
from animation import CharacterAnimation


def image(direction):
    if direction == "left":
        image = pygame.image.load(
            "assets\\character_animation\\blue\\idle\\idle1.png").convert_alpha()
        image = pygame.transform.scale2x(image)
        image = pygame.transform.flip(image, True, False)
    elif direction == "right":
        image = pygame.image.load(
            "assets\\character_animation\\blue\\idle\\idle1.png").convert_alpha()
        image = pygame.transform.scale2x(image)
    elif direction == "tree":
        image = pygame.image.load(
            "assets\Parallax\Alien_tileset_tree_06.png").convert_alpha()
        # image = pygame.transform.flip(image, True, False)
        # image = pygame.transform.scale2x(image)
    elif direction == "jump":
        image = pygame.image.load(
            "assets\character animation\jump\jump5.png").convert_alpha()
        image = pygame.transform.scale2x(image)
    elif direction == "land":
        image = pygame.image.load(
            "assets\Parallax\\aliens_ground_04-modified.png").convert_alpha()
    elif direction == 'door':
        image = pygame.image.load(
            "assets\Parallax\door_02-modified.png").convert_alpha()
    elif direction == "big_land":
        image = pygame.image.load(
            "assets\Parallax\\aliens_big_ground_7-modified.png").convert_alpha()
    elif direction == "eater":
        image = []
        for i in range(1, 13):
            image.append(pygame.image.load(
                f"assets\Parallax\eater_{i}-modified.png").convert_alpha())
    elif direction == "flying":
        image = []
        for i in range(1, 5):
            image.append(pygame.image.load(
                f"assets\Parallax\\flying_bot_{i}-modified.png").convert_alpha())
    elif direction == "slime":
        image = []
        for i in range(1, 5):
            image.append(pygame.image.load(
                f"assets\Parallax\slime_{i}-modified.png").convert_alpha())
    return image


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.move_set = {
                        "attack": CharacterAnimation(8, "red", "attack"),
                        "damage": CharacterAnimation(4, "red", "damage"),
                        "death": CharacterAnimation(12, "red", "death"),
                        "idle": CharacterAnimation(6, "red", "idle"),
                        "jump_down": CharacterAnimation(8, "red", "jump_down"),
                        "jump_up": CharacterAnimation(8, "red", "jump_up"),
                        "run": CharacterAnimation(8, "red", "run"),
                        "shield": CharacterAnimation(3, "red", "shield")
                        }
        self.image = image("right")
        self.rect = self.image.get_rect(
            midbottom=(300, SCREEN_HEIGHT - (ground_height)))
        self.player_x = x
        self.player_y = y
        self.hit_box = pygame.Rect((self.player_x+36, self.player_y+48), (44, 64))
        self.attack_hit_box = pygame.Rect((self.player_x+80, self.player_y+48), (28, 64))
        self.on_ground = True

    def update(self):
        self.player_x = 0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.player_x = -5
            self.image = image("left")

        if keys[pygame.K_RIGHT]:
            self.player_x = 5
            self.image = image("right")

        # Jumping
        if keys[pygame.K_SPACE] and self.on_ground:
            self.y_velocity = -18
            self.on_ground = False
            # self.image = image("jump")

        # Apply gravity
        self.y_velocity += 0.8

        # Limit the vertical speed
        if self.y_velocity > 10:
            self.y_velocity = 10

        self.rect.x += self.player_x
        self.rect.y += self.y_velocity

        # fdsfsdf
        if self.rect.left < 200:
            self.rect.left = 200
        # dsfsdf
        if self.rect.right > 1000:
            self.rect.right = 1000

    def draw(self, screen):
        print(self.move_set["attack"].run_animation(screen, (500, 100)))
        pygame.draw.rect(screen, (0, 0, 255), self.hit_box, 2)
        pygame.draw.rect(screen,(0,255,0),self.attack_hit_box,2)



if __name__ == "__main__":
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Spritesheets')
    BG = (150, 50, 5)

    ground_image = pygame.image.load(
        "assets\Parallax\\aliens_ground_04-modified.png").convert_alpha()
    ground_width = ground_image.get_width()
    ground_height = ground_image.get_height()

    player = Player(500, 100)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill(BG)

        player.draw(screen)

        pygame.display.update()
    pygame.quit()
