import pygame
from game_menu import StartGameMenu
from sys import exit


def quit_game():
    pygame.quit()
    exit()
        
# this is the main function
def main():
    pygame.display.set_caption("Pixel Rampage")
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width,screen_height))
    start_game_menu = StartGameMenu()
    game_state = "start_game"

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
                #puase menu events handler
                pass


            
                #######################################################

                # game background and ground event handler





                #######################################################

                
        if game_state == "start_game":
            start_game_menu.start_game_draw(screen,screen_width,screen_height)
        elif game_state == "playing":
            screen.fill((0, 0, 0)) #this line here is to fill the screen with black
            # puase menu draw



            ######################################################

            #background and ground draw







            ######################################################


        pygame.display.update()

if __name__ == "__main__":
    main()