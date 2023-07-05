import pygame
from game_objects import Ground


pygame.init()


class Player:
    def __init__(self, color, position,control):
        animation_path = f"assets\\character_animation\\{color}"
        self.attack_animation = [pygame.transform.scale2x(pygame.image.load(
            f"{animation_path}\\attack\\attack{number}.png").convert_alpha()) for number in range(3)]
        self.running_animation = [pygame.transform.scale2x(pygame.image.load(
            f"{animation_path}\\run\\run{number}.png").convert_alpha()) for number in range(1,9)]
        self.idle_animation = [pygame.transform.scale2x(pygame.image.load(
            f"{animation_path}\\idle\\idle{number}.png").convert_alpha()) for number in range(1,7)]
        self.damage_animation = [pygame.transform.scale2x(pygame.image.load(
            f"{animation_path}\\damage\\damage{number}.png").convert_alpha()) for number in range(1,5)]
        self.jump_animation = [pygame.transform.scale2x(pygame.image.load(f"{animation_path}\\jump\\jump{number}.png").convert_alpha()) for number in range(1,4)]
        self.rect = self.attack_animation[0].get_rect(midbottom=position)
        self.defult_position = position

        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100
        self.frame = 0

        self.x_velocity = 0
        self.y_velocity = 0
        self.on_ground = False

        self.control_buttons = control
        self.running_speed = 10
        self.jumping_speed = 18
        self.attack_state = False
        self.fleped = False
        self.current_move = self.idle_animation
        self.hit_box = pygame.Rect((self.rect.x+36, self.rect.y+48), (44, 64))
        self.attack_hit_box = pygame.Rect(
            (self.rect.x+80, self.rect.y+48), (28, 64))
        
    def move_right(self):
        self.x_velocity = 5
        if self.fleped:
            self.fleped = False
        if self.on_ground:
            self.current_move = self.running_animation

    def move_left(self):
        self.x_velocity = -5
        if not self.fleped:
            self.fleped = True
        if self.on_ground:
            self.current_move = self.running_animation
        

    def jump_up(self):
        self.y_velocity = -18
        self.on_ground = False
        self.current_move = self.jump_animation

    def idle(self):
        self.current_move = self.idle_animation

    def attack(self):
        self.current_move = self.attack_animation
        self.x_velocity = 0
        self.y_velocity = 0

    def ground_collide(self,rects):
        # print(rects)
        if any(self.hit_box.colliderect(rect) and rect.top<=self.hit_box.bottom for rect in rects):
            # print("collide")
            self.on_ground = True
            self.y_velocity = 0
        else:
            # print("not collide")
            self.on_ground = False
            
            

    def get_player_position(self):
        return self.rect.x
    
    def get_rect(self):
        return self.rect
    
    def reset_position(self):
        self.rect = self.attack_animation[0].get_rect(midbottom=self.defult_position)
        self.hit_box = pygame.Rect((self.rect.x+36, self.rect.y+48), (44, 64))
        self.attack_hit_box = pygame.Rect((self.rect.x+80, self.rect.y+48), (28, 64))


    def movment(self,rects):
        self.x_velocity = 0
        keys=pygame.key.get_pressed()
        input_buttons = [keys[button] for  button in self.control_buttons]

        self.ground_collide(rects)

        if input_buttons[3] and self.on_ground or self.attack_state:
            if self.current_move != self.attack_animation:
                self.frame = 0
            if self.frame < len(self.attack_animation)-1:
                self.attack_state = True
            else:
                self.attack_state = False
            self.attack()
            return

        if input_buttons[0]:
            if self.current_move != self.running_animation:
                self.frame = 0
            self.move_left()
            
        elif input_buttons[1]:
            if self.current_move != self.running_animation:
                self.frame = 0
            self.move_right()

        if input_buttons[2] and self.on_ground:
            if self.current_move != self.jump_animation:
                self.frame = 0
            self.jump_up()
        

        if self.x_velocity == 0 and self.on_ground:
            if self.current_move != self.idle_animation:
                self.frame = 0
            self.idle()

        if not self.on_ground:
            self.y_velocity += 0.8

		# Limit the vertical speed
        if self.y_velocity > 20:
            self.y_velocity = 20

        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity
        self.hit_box.x += self.x_velocity
        self.hit_box.y += self.y_velocity
        self.attack_hit_box.x += self.x_velocity
        self.attack_hit_box.y += self.y_velocity

    def draw(self, screen):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.frame = (self.frame + 1) % len(self.current_move)
            self.last_update = current_time
        image = self.current_move[self.frame]
        image = pygame.transform.flip(image, self.fleped, False)
        screen.blit(image, self.rect)
        pygame.draw.rect(screen, (255, 0, 0), self.hit_box, 2)
        pygame.draw.rect(screen, (0, 0, 255), self.attack_hit_box, 2)



if __name__ == "__main__":
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('player test')
    BG = (150, 50, 5)
    clock = pygame.time.Clock()
    FPS = 60

    player = Player("blue", (50, 200),[pygame.K_a, pygame.K_d, pygame.K_SPACE, pygame.K_f])
    # player2 = Player("red", (100, 200),[pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_RSHIFT])
    grounds = [Ground("assets\\grounds\\ground1.png", (500*(number), 400)) for number in range(10)]

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill(BG)

        # player.movment()
        player.draw(screen)
        # player2.draw(screen)
        for ground in grounds:
            ground.draw(screen)

        
        
        # player.ground_collide()
        # player2.ground_collide(grounds)
        player.movment(grounds)
        # player2.movment()
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
