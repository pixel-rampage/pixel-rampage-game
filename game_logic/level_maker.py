import pygame
from game_objects import LevelObject, Ground, Coin,Key
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
        self.keys = []
        self.collected_coins = []
        self.collected_key = []


    def add_ground(self, image, position):
        self.ground_images.append(Ground(image, position))

    def add_level_object(self, image, position):
        self.level_objects.append(LevelObject(image, position))

    def add_coin(self, image, position):
        self.coins.append(Coin(image, position))

    def add_key(self, image, position):
        self.keys.append(Key(image,position))


    def get_grounds_rect(self):
        return [rect.get_rect() for rect in self.ground_images]

    def collect_coin(self, rect):
        collected_coin = rect.collidelist(self.coins)
        if collected_coin != -1:
            self.collected_coins.append(self.coins.pop(collected_coin))
    
    def collect_key(self, rect):
        collected_key = rect.collidelist(self.keys)
        if collected_key != -1:
            self.collected_key.append(self.keys.pop(collected_key))

    def level_reset(self):
        for coins in self.collected_coins:
            self.coins.append(self.collected_coins.pop())
        for key in self.collected_key:
            self.keys.append(self.collected_key.pop())
        for background in self.background_images:
            background.reset_position()
        for ground in self.ground_images:
            ground.reset_position()
        for object in self.level_objects:
            object.reset_position()
        for coin in self.coins:
            coin.reset_position()
        for key in self.keys:
            key.reset_position()

    def update_position(self,player_rect):
        direction = None
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and player_rect.right > 999:
            direction = True
        elif keys[pygame.K_a] and self.background_images[0].background_rects.x < 0 and player_rect.left < 201:
            direction = False


        for background in self.background_images:
            background.update_position(direction)

        for ground in self.ground_images:
            ground.update_position(direction)

        for object in self.level_objects:
            object.update_position(direction)

        for coin in self.coins:
            coin.update_position(direction)

        for key in self.keys:
            key.update_position(direction)


    def draw(self, screen):
        for background in self.background_images:
            background.draw(screen)

        for object in self.level_objects:
            object.draw(screen)

        for ground in self.ground_images:
            ground.draw(screen)

        for coin in self.coins:
            coin.draw(screen)

        for key in self.keys:
            key.draw(screen)