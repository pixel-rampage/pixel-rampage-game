import pygame
from game_menu import Menus


# this function job is to close the game
def quit_game():
    pygame.quit()
    exit()

#this function job is to display the start game menu
def start_game(screen, screen_width, screen_height, buttons_path, text_color):
    menus = Menus()
    logo, font_rect, button_play_image, button_play_image_rect, play_game_text, play_game_text_rect, button_quit_image, button_quit_image_rect, quit_text, quit_text_rect = menus.start_game_menu(buttons_path,screen_width,screen_height,text_color)
    screen.blit(logo,font_rect)
    screen.blit(button_play_image,button_play_image_rect)
    screen.blit(play_game_text, play_game_text_rect)
    screen.blit(button_quit_image,button_quit_image_rect)
    screen.blit(quit_text,quit_text_rect)
    return button_play_image_rect, button_quit_image_rect


# this function job is to handle the event for the start game menu
def start_game_events(event, button_rect1, button_rect2, buttons_path, text_color, game_state):
    if event.type == pygame.MOUSEMOTION:
        if button_rect1.collidepoint(event.pos):
            buttons_path = ("assets\\menu_assets\\button_on.png",buttons_path[1])
            text_color = ("#CD7F32",text_color[1])
        elif button_rect2.collidepoint(event.pos):
            buttons_path = (buttons_path[0],"assets\\menu_assets\\button_on.png")
            text_color = (text_color[0],"#CD7F32")
        else:
            buttons_path = ("assets\\menu_assets\\button_off.png","assets\\menu_assets\\button_off.png")
            text_color = ("#F5F5F5","#F5F5F5")
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1 and button_rect2.collidepoint(pygame.mouse.get_pos()):
            quit_game()
        if event.button == 1 and button_rect1.collidepoint(pygame.mouse.get_pos()):
            game_state = "playing"

    return buttons_path, text_color, game_state

        
# this is the main function
def main():
    pygame.display.set_caption("Pixel Rampage")
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width,screen_height))
    buttons_path = ("assets\\menu_assets\\button_off.png","assets\\menu_assets\\button_off.png")
    text_color = ("#F5F5F5","#F5F5F5")
    start_game_rect1 = start_game_rect2 = None
    game_state = "start_game"

    while True:
        if game_state == "start_game":
            start_game_rect1,start_game_rect2 = start_game(screen,screen_width,screen_height, buttons_path, text_color)
        elif game_state == "playing":
            screen.fill((0, 0, 0)) #this line here is to fill the screen with black
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if game_state == "start_game":
                buttons_path, text_color, game_state = start_game_events(event, start_game_rect1, start_game_rect2, buttons_path, text_color, game_state)

        pygame.display.update()

if __name__ == "__main__":
    main()