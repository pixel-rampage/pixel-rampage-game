import pygame
from game_objects import LevelObject,Ground
from level_background import LevelBackground

pygame.init()


class LevelMaker:
    def __init__(self, screen_width, screen_height, background_type):
        self.screen_width, self.screen_height = screen_width, screen_height
        self.background_images = [LevelBackground(
            screen_width, screen_height, background_type, position) for position in range(11)]
        self.ground_images = []
        self.level_objects = []
        self.coins = []

    def add_ground(self, image, position):
        self.ground_images.append(Ground(image, position))

    def add_level_object(self, image, position):
        self.level_objects.append(LevelObject(image, position))

    def get_grounds_rect(self):
        return [rect.get_rect() for rect in self.ground_images]
    
    def level_reset(self):
        for background in self.background_images:
            background.reset_position()
        for ground in self.ground_images:
            ground.reset_position()
        for object in self.level_objects:
            object.reset_position()

    def update_position(self):
        direction = None
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            direction = True
        elif keys[pygame.K_a] and self.background_images[0].background_rects.x < 0:
            direction = False

        for background in self.background_images:
            background.update_position(direction)

        for ground in self.ground_images:
            ground.update_position(direction)

        for object in self.level_objects:
            object.update_position(direction)

    def draw(self, screen):
        for background in self.background_images:
            background.draw(screen)

        for object in self.level_objects:
            object.draw(screen)

        for ground in self.ground_images:
            ground.draw(screen)

