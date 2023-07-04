import pygame

pygame.init()

class LevelObject:
    def __init__(self, image, position):
        self.ground_image = pygame.image.load(image).convert_alpha()
        self.ground_rect = self.ground_image.get_rect(midbottom=position)
        self.defult_position = position

    def update_position(self, direction):
        if direction == True:
            self.ground_rect.x -= 5
        elif direction == False:
            self.ground_rect.x += 5
    
    def reset_position(self):
        self.ground_rect = self.ground_image.get_rect(midbottom=self.defult_position)

    def draw(self, screen):
        screen.blit(self.ground_image, self.ground_rect)


class Ground(LevelObject):
    def __init__(self, image, position):
        super().__init__(image,position)

    def get_rect(self):
        return self.ground_rect