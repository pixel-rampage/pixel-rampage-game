import pygame

pygame.init()

class Button:
    def __init__(self, button_text, position, button_image):
        self.font = pygame.font.Font("assets\\fonts\game_over.ttf", 128)
        self.button_text = button_text
        button_stats = ["off.png", "on.png"]
        self.selected_button = 0
        self.buttons_images = [pygame.image.load(
            button_image+button_images_stats).convert_alpha() for button_images_stats in button_stats]
        self.text = self.font.render(button_text, True, "#F5F5F5")
        self.button_rect = self.buttons_images[0].get_rect(center=position)
        text1_pos = (position[0], position[1]-(position[1]*0.02))
        self.text_rect = self.text.get_rect(center=text1_pos)

    def hover(self):
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            self.selected_button = 1
            self.text = self.font.render(self.button_text, False, "#CD7F32")
        else:
            self.selected_button = 0
            self.text = self.font.render(self.button_text, False, "#F5F5F5")

    def button_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos) and event.button == 1:
                return True
            else:
                return False

    def draw(self, screen):
        screen.blit(
            self.buttons_images[self.selected_button], self.button_rect)
        screen.blit(self.text, self.text_rect)


class Menu:
    def __init__(self, screen_width, screen_height, font_size):
        self.font = pygame.font.Font("assets\\fonts\game_over.ttf", font_size)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.buttons = []

    def add_button(self, button_text, position, button_type):
        self.buttons.append(Button(button_text, position, button_type))


# start menu class
class StartGameMenu(Menu):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height, 128)
        self.background_frame = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100
        self.backgroung_imag = [pygame.image.load(
            f'assets\\backgrounds\\start_game_background\\start_game_background_{image_number}.png').convert_alpha() for image_number in range(1, 12)]
        self.background_rect = self.backgroung_imag[0].get_rect(topleft=(0, 0))
        self.add_button("Play", (screen_width*0.5, screen_height * 0.45), "assets\\menu_assets\\button_")
        self.add_button("Quit", (screen_width * 0.5, screen_height * 0.7), "assets\\menu_assets\\button_")

    def logo_info(self, position):
        logo = self.font.render("Pixel Rampage", False, "#F5F5F5")
        logo_rect = logo.get_rect(midtop=position)
        return logo, logo_rect

    def start_game_draw(self, screen):
        logo, logo_rect = self.logo_info(
            (self.screen_width*0.5, self.screen_height*0.15))
        screen.blit(self.backgroung_imag[self.background_frame % 11], self.background_rect)
        screen.blit(logo, logo_rect)
        for button in self.buttons:
            button.draw(screen)
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.background_frame = (self.background_frame + 1) % 11
            self.last_update = current_time

# Pause menu class
class PauseGameMenu(Menu):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height, 128)
        self.backgroung_imag = pygame.image.load(
            'assets\menu_assets\pause_menu.png').convert_alpha()
        self.background_rect = self.backgroung_imag.get_rect(
            center=(screen_width*0.5, screen_height*0.48))
        self.add_button("Resume", (screen_width*0.5,
                        screen_height*0.45), "assets\\menu_assets\\button_")
        self.add_button("Main Menu", (screen_width * 0.5,
                        screen_height * 0.7), "assets\\menu_assets\\button_")

    def menu_text(self, position):
        text = self.font.render("Pause Game", False, "#505050")
        text_rect = text.get_rect(midtop=position)
        return text, text_rect

    def pause_game_draw(self, screen):
        text, text_rect = self.menu_text(
            (self.screen_width*0.5, self.screen_height*0.15))
        width, height = self.backgroung_imag.get_size()
        self.backgroung_imag = pygame.transform.scale(
            self.backgroung_imag, (width, self.screen_height*0.6))
        screen.blit(self.backgroung_imag, self.background_rect)
        screen.blit(text, text_rect)
        for button in self.buttons:
            button.draw(screen)

# Game Over menu class
class GameOverMenu(Menu):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height, 256)
        self.background_frame = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100
        self.backgroung_imag = [pygame.image.load(
            f'assets\\backgrounds\\game_over_background\\game_over_ground{image_number}.png').convert_alpha() for image_number in range(1, 28)]
        self.background_rect = self.backgroung_imag[0].get_rect(topleft=(0, 0))
        self.add_button("Play Again", (screen_width*0.5, screen_height *
                        0.35), "assets\\menu_assets\\game_over_button_")
        self.add_button("Main Menu", (screen_width * 0.5, screen_height *
                        0.6), "assets\\menu_assets\\game_over_button_")

    def menu_text(self, position):
        text = self.font.render("Game Over", False, "#F5F5F5")
        text_rect = text.get_rect(center=position)
        return text, text_rect

    def game_over_draw(self, screen):
        text, text_rect = self.menu_text(
            (self.screen_width*0.5, self.screen_height*0.07))
        scaled_background = pygame.transform.scale(
            self.backgroung_imag[self.background_frame % 27], (self.screen_width, self.screen_height))
        screen.blit(scaled_background, self.background_rect)
        screen.blit(text, text_rect)
        for button in self.buttons:
            button.draw(screen)
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.background_frame = (self.background_frame + 1) % 11
            self.last_update = current_time
