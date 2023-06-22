import pygame
from game_menu import Menus


def main():
    pygame.display.set_caption("Pixel Rampage")
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width,screen_height))
    menus = Menus()
    buttons_path = ("assets\\menu_assets\\button_off.png","assets\\menu_assets\\button_off.png")
    text_color = "#F5F5F5"

    while True:
        logo, font_rect, button_play_image, button_play_image_rect, play_game_text, play_game_text_rect, button_quit_image, button_quit_image_rect, quit_text, quit_text_rect = menus.start_game_menu(buttons_path,screen_width,screen_height,text_color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEMOTION:
                if button_play_image_rect.collidepoint(event.pos):
                    buttons_path = ("assets\\menu_assets\\button_on.png",buttons_path[1])
                    text_color = "#CD7F32"
                elif button_quit_image_rect.collidepoint(event.pos):
                    buttons_path = (buttons_path[0],"assets\\menu_assets\\button_on.png")
                    text_color = "#CD7F32"
                else:
                    buttons_path = ("assets\\menu_assets\\button_off.png","assets\\menu_assets\\button_off.png")
                    text_color = "#F5F5F5"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and button_quit_image_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    exit()
                if event.button == 1 and button_play_image_rect.collidepoint(pygame.mouse.get_pos()):
                    print("play")
                
                

                

        screen.blit(logo,font_rect)
        screen.blit(button_play_image,button_play_image_rect)
        screen.blit(play_game_text, play_game_text_rect)
        screen.blit(button_quit_image,button_quit_image_rect)
        screen.blit(quit_text,quit_text_rect)
        

        pygame.display.update()

if __name__ == "__main__":
    main()