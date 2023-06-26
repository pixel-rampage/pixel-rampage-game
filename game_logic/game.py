import pygame
from game_menu import StartGameMenu, PauseGameMenu
from sys import exit
import threading


class Background:
    def __init__(self, screen_width, screen_height):
        self.scroll = 0
        self.bg_images = [pygame.transform.scale(pygame.image.load(
            f"assets\Parallax/{i}.png").convert_alpha(), (screen_width, screen_height)) for i in range(1, 8)]
        self.bg_width = self.bg_images[0].get_width()
        self.lock = threading.Lock()

    def draw_bg(self, screen):
        with self.lock:
            for x in range(8):
                speed = 1
                for i in self.bg_images:
                    screen.blit(
                        i, ((x * self.bg_width) - self.scroll * speed, 0))
                    speed += 0.1

    def update_bg(self):
        # Get keypresses
        with self.lock:
            key = pygame.key.get_pressed()
            if key[pygame.K_RIGHT] and self.scroll <5000:
                self.scroll += 5
            elif key[pygame.K_LEFT] and self.scroll > 0:
                self.scroll -= 5


def quit_game():
    pygame.quit()
    exit()

# this is the main function


def main():
    pygame.display.set_caption("Pixel Rampage")
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    start_game_menu = StartGameMenu(screen_width, screen_height)
    pause_menu = PauseGameMenu(screen_width, screen_height)
    background = Background(screen_width, screen_height)
    game_state = "start_game"
    pause_or_not = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if game_state == "start_game":
                start_game_menu.play_button.hover()
                start_game_menu.quit_button.hover()
                if start_game_menu.play_button.button_clicked(event):
                    game_state = "playing"
                if start_game_menu.quit_button.button_clicked(event):
                    quit_game()
            elif game_state == "playing":
                # puase menu events handler
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause_or_not = True
                if pause_menu.resume_button.button_clicked(event):
                    pause_or_not = False
                if pause_menu.quit_button.button_clicked(event):
                    pause_or_not = False
                    game_state = "start_game"

        if game_state == "start_game":
            screen.fill((0, 0, 0))
            start_game_menu.start_game_draw(screen)
        elif game_state == "playing":
            # this line here is to fill the screen with black
            # screen.fill((0, 0, 0))
            background.update_bg()
            background.draw_bg(screen)
            if pause_or_not:
                pause_menu.resume_button.hover()
                pause_menu.quit_button.hover()
                pause_menu.pause_game_draw(screen)

        pygame.display.update()


if __name__ == "__main__":
    main()
