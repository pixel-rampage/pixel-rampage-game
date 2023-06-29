import pygame

class AnimationGame:
    def __init__(self):
        pygame.init()
        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 720
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption('Spritesheets')
        self.BG = (150, 50, 5)
        self.animation_list = []
        self.animation_steps = 6
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100
        self.frame = 0

    def load_animation_images(self, animation_folder, steps):
        self.animation_list = []
        for x in range(steps):
            image_path = f'assets/character animation/{animation_folder}/{animation_folder}{x+1}.png'
            image = pygame.transform.scale(pygame.image.load(image_path), (200, 200)).convert_alpha()
            self.animation_list.append(image)

    def run_animation(self):
        run = True
        while run:
            self.screen.fill(self.BG)
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update >= self.animation_cooldown:
                self.frame = (self.frame + 1) % self.animation_steps
                self.last_update = current_time
            self.screen.blit(self.animation_list[self.frame], (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.update()

        pygame.quit()

# Create an instance of the AnimationGame class and run the game
game = AnimationGame()

# Load and run falling animation
# game.load_animation_images('falling',8)

# Load and run jump animation
# game.load_animation_images('jump',8)

# Load and run running animation
# game.load_animation_images('running',8)

# Load and idel running animation
game.load_animation_images('idel',6)
game.run_animation()
