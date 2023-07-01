import pygame
from animation import CharacterAnimation

class Player:
    def __init__(self):
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
        self.rect = self.move_set["idle"].make_rect((300,600))
        self.control_buttons = [pygame.K_a,pygame.K_d,pygame.K_SPACE,pygame.K_f]
        self.fleped = False
        self.on_ground = True
        self.current_move = self.move_set["idle"]
        self.animation_is_done = False
        self.running_speed = 5
        self.jump_speed = 18
        self.hit_box = pygame.Rect((self.rect.x+36, self.rect.y+48), (44, 64))
        self.attack_hit_box = pygame.Rect((self.rect.x+80, self.rect.y+48), (28, 64))

    def move_right(self):
        self.rect.x += self.running_speed
        self.hit_box.x += self.running_speed
        if self.hit_box.x > self.attack_hit_box.x:
            self.attack_hit_box = pygame.Rect((self.hit_box.x+44, self.hit_box.y), (28, 64))
        else:
            self.attack_hit_box.x += self.running_speed
        if self.fleped:
            self.fleped = False
        self.current_move = self.move_set["run"]

    def move_left(self):
        self.rect.x -= self.running_speed
        self.hit_box.x -= self.running_speed
        if self.hit_box.x < self.attack_hit_box.x:
            self.attack_hit_box = pygame.Rect((self.hit_box.x-28, self.hit_box.y), (28, 64))
        else:
            self.attack_hit_box.x -= self.running_speed
        if not self.fleped:
            self.fleped = True
        self.current_move = self.move_set["run"]

    def jump_up(self):
        self.current_move = self.move_set["jump_up"]
        if (self.current_move.frame + 1)% self.current_move.animation_steps == 0:
            self.on_ground = False

    def jump_down(self):
        self.current_move = self.move_set["jump_down"]
        if (self.current_move.frame + 1)% self.current_move.animation_steps == 0:
            self.on_ground = True

    def attack(self):
        self.current_move = self.move_set["attack"]
        if (self.current_move.frame + 1)% self.current_move.animation_steps == 0:
            self.animation_is_done = True

    def rest(self):
        # keys=pygame.key.get_pressed()
        # input_buttons = [keys[button] for button in self.control_buttons]
        # if all(button == False for button in input_buttons):
        self.current_move = self.move_set["idle"]
        for value in self.move_set.values():
            if value != self.current_move:
                value.frame = 0
    
    def movment(self):
        keys=pygame.key.get_pressed()
        input_buttons = [keys[button] for button in self.control_buttons]
        if keys[pygame.K_a]:
            self.move_left()
            
        elif keys[pygame.K_d]:
            self.move_right()
        
        elif keys[pygame.K_f] or self.animation_is_done and self.current_move == self.move_set["attack"]:
            self.attack()
        

        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump_up()
            
        
        if not self.on_ground:
            self.jump_down()

        if all(button == False for button in input_buttons) and self.on_ground:
            self.rest()

    def draw(self,screen):
        self.current_move.run_animation(screen,self.rect,self.fleped)
        pygame.draw.rect(screen, (255,0,0), self.hit_box,2)
        pygame.draw.rect(screen, (0,0,255), self.attack_hit_box,2)
        





if __name__ == "__main__":
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Spritesheets')
    BG = (150, 50, 5)
    clock = pygame.time.Clock()
    FPS = 60

    player = Player()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill(BG)


        player.movment()
        player.draw(screen)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
