import pygame
from sys import exit
clock = pygame.time.Clock()

# joystick zone joystick zone joystick zone joystick zone joystick zone joystick zone joystick zone
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i)
             for i in range(pygame.joystick.get_count())]


def check_if_jump():
    for joy in joysticks:
        if joy.get_button(0):
            return True
        else:
            return False


def check_if_run_right():
    for joy in joysticks:
        if round(joy.get_axis(0)) > 0:
            return True
        else:
            return False


def check_if_run_left():
    for joy in joysticks:
        if round(joy.get_axis(0)) < 0:
            return True
        else:
            return False
# joystick zone joystick zone joystick zone joystick zone joystick zone joystick zone joystick zone
# joystick zone joystick zone joystick zone joystick zone joystick zone joystick zone joystick zone


# walk animation
walk_right = [pygame.transform.scale2x(pygame.image.load(
    f'assets\\character_animation\\biue\\run\\char_blue_{number}.png')) for number in range(1, 9)]
walk_left = [pygame.transform.flip(walk, True, False) for walk in walk_right]

# jump animation
jump_animation_right = [pygame.transform.scale2x(pygame.image.load(
    f'assets\\character_animation\\biue\\jump\\char_blue_jump_up_{number}.png')) for number in range(1, 9)]
jump_animation_left = [pygame.transform.flip(
    jump, True, False) for jump in jump_animation_right]

# idel animation
idel_right = [pygame.transform.scale2x(pygame.image.load(
    f'assets\\character_animation\\biue\\idle\\char_blue_idle_{number}.png')) for number in range(1, 7)]
idel_left = [pygame.transform.flip(idel, True, False) for idel in idel_right]


class Player(object):
    def __init__(self, player_x, player_y, player_width, player_height, name=None):
        self.player_x = player_x
        self.player_y = player_y
        self.player_width = player_width
        self.player_height = player_height
        self.player_velocity = 5
        # state
        self.isjump = False            # state
        self.left = False              # state
        self.right = False             # state
        self.direction = "right"         # state
        # counter
        self.walk_count = 0  # counter
        self.jump_animation_count = 0  # counter
        self.idel_count = 0  # counter
        self.jump_count = 10  # counter

        self.hitbox = (self.player_x + 47, self.player_y + 41, 59, 82)
        self.name = name

    def draw(self, win):
        # counters
        if self.walk_count + 1 >= 24:
            self.walk_count = 0
        if self.jump_animation_count + 1 >= 24:
            self.jump_animation_count = 0
        if self.idel_count + 1 >= 18:
            self.idel_count = 0

         # idel animation :right
        if self.isjump == False and self.right == False and self.left == False and self.direction == "right":
            win.blit(idel_right[self.idel_count//3],
                     (self.player_x, self.player_y))
            self.idel_count += 1

         # idel animation left
        elif self.isjump == False and self.right == False and self.left == False and self.direction == "left":
            win.blit(idel_left[self.idel_count//3],
                     (self.player_x, self.player_y))
            self.idel_count += 1

        # jump and right animation
        elif self.isjump and self.right:
            win.blit(
                jump_animation_right[self.jump_animation_count//3], (self.player_x, self.player_y))
            self.jump_animation_count += 1
            self.direction = "right"
        # jump and left animation
        elif self.isjump and self.left:
            win.blit(
                jump_animation_left[self.jump_animation_count//3], (self.player_x, self.player_y))
            self.jump_animation_count += 1
            self.direction = "left"
         # idel jump : right
        elif self.isjump and self.direction == 'right':
            win.blit(
                jump_animation_right[self.jump_animation_count//3], (self.player_x, self.player_y))
            self.jump_animation_count += 1
         # idel jump left
        elif self.isjump and self.direction == 'left':
            win.blit(
                jump_animation_left[self.jump_animation_count//3], (self.player_x, self.player_y))
            self.jump_animation_count += 1
        # running left
        elif self.left:
            win.blit(walk_left[self.walk_count//3],
                     (self.player_x, self.player_y))
            self.walk_count += 1
         # running left
        elif self.right:
            win.blit(walk_right[self.walk_count//3],
                     (self.player_x, self.player_y))
            self.walk_count += 1
        self.hitbox = (self.player_x + 47, self.player_y + 41, 59, 82)

    def player_move(self):
        keys = pygame.key.get_pressed()

    #  self.player_y +=10
        if self.name == 'player_one':
            self.left = False
            self.right = False
            if keys[pygame.K_LEFT] or check_if_run_left():
                self.player_x -= self.player_velocity
                self.left = True
                self.right = False
                self.direction = 'left'
            elif keys[pygame.K_RIGHT] or check_if_run_right():
                self.player_x += self.player_velocity
                self.right = True
                self.left = False
                self.direction = 'right'
            else:
                self.walk_count = 0
            if not (self.isjump):
                if keys[pygame.K_UP] or check_if_jump():
                    self.isjump = True
                    self.right = False
                    self.left = False
                    self.walk_count = 0
            else:
                if self.jump_count >= -10:
                    negative = 1
                    if self.jump_count < 0:
                        negative = -1
                    self.player_y -= (self.jump_count**2)*0.4 * negative
                    self.jump_count -= 1
                else:
                    self.isjump = False
                    self.jump_count = 10
        elif self.name == 'player_two':
            self.left = False
            self.right = False
            if keys[pygame.K_a]:
                self.player_x -= self.player_velocity
                self.left = True
                self.right = False
                self.direction = 'left'
            elif keys[pygame.K_d]:
                self.player_x += self.player_velocity
                self.right = True
                self.left = False
                self.direction = 'right'
            else:
                self.walk_count = 0
            if not (self.isjump):
                if keys[pygame.K_SPACE]:
                    self.isjump = True
                    self.right = False
                    self.left = False
                    self.walk_count = 0
            else:
                if self.jump_count >= -10:
                    negative = 1
                    if self.jump_count < 0:
                        negative = -1
                    self.player_y -= (self.jump_count**2)*0.4 * negative
                    self.jump_count -= 1
                else:
                    self.isjump = False
                    self.jump_count = 10


def redrawGameWindow(screen, player, player2):
    screen.fill((0, 0, 0))
    player.draw(screen)
    player2.draw(screen)


def quit_game():
    pygame.quit()
    exit()

# this is the main function


def main():
    player_one = Player(200, 500, 56, 56, 'player_one')
    player_two = Player(200, 500, 56, 56, 'player_two')
    pygame.display.set_caption("Pixel Rampage")
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        pygame.display.update()


if __name__ == "__main__":
    main()
