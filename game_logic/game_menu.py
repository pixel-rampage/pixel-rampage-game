import pygame
from sys import exit

pygame.init()

class Menus:
    def __init__(self):
          self.font = pygame.font.Font("assets\\fonts\game_over.ttf",128)

    def logo(self):
        pass

    def button(self, position, img, button_text,text_color):
        text = self.font.render(button_text,True,text_color)
        button_image = pygame.image.load(img)
        button_image_rect = button_image.get_rect(center=position)
        text1_pos =(position[0], position[1]-(position[1]*0.02))
        text_rect = text.get_rect(center = text1_pos)
        return button_image,button_image_rect,text,text_rect


    def draw(self):
        pass  
    
    def start_game_menu(self,buttons_path,screen_width,screen_height,text_color):
        logo = self.font.render("Pixel Rampage",False,"#F5F5F5")
        logo_rect = logo.get_rect(midtop = (screen_width*0.5,screen_height*0.15))
        button_play_image,button_play_image_rect,play_game_text,play_game_text_rect = self.button((screen_width*0.5, screen_height*0.45),buttons_path[0],"Play",text_color)
        button_quit_image,button_quit_image_rect,quit_text,quit_text_rect = self.button((screen_width * 0.5, screen_height * 0.7),buttons_path[1],"Quit",text_color)
        return logo, logo_rect, button_play_image, button_play_image_rect, play_game_text, play_game_text_rect, button_quit_image, button_quit_image_rect, quit_text, quit_text_rect
        # screen.blit(logo,font_rect)
        # screen.blit(button_play_image,button_play_image_rect)
        # screen.blit(play_game_text, play_game_text_rect)
        # screen.blit(button_quit_image,button_quit_image_rect)
        # screen.blit(quit_text,quit_text_rect)
        
        
        

          


if __name__ == "__main__":
    pygame.display.set_caption("Pixel Rampage")
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width,screen_height))
    menus = Menus()
    buttons_path = ("assets\\menu_assets\\button_off.png","assets\\menu_assets\\button_off.png")
    text_color = "#F5F5F5"

    while True:
        logo, logo_rect, button_play_image, button_play_image_rect, play_game_text, play_game_text_rect, button_quit_image, button_quit_image_rect, quit_text, quit_text_rect = menus.start_game_menu(buttons_path,screen_width,screen_height, text_color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEMOTION:
                if button_play_image_rect.collidepoint(event.pos):
                    buttons_path = ("assets\\menu_assets\\button_on.png",buttons_path[1])
                elif button_quit_image_rect.collidepoint(event.pos):
                    buttons_path = (buttons_path[0],"assets\\menu_assets\\button_on.png")
                else:
                    buttons_path = ("assets\\menu_assets\\button_off.png","assets\\menu_assets\\button_off.png")

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and button_quit_image_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    exit()
                if event.button == 1 and button_play_image_rect.collidepoint(pygame.mouse.get_pos()):
                    print("play")
                
                

                

        screen.blit(logo,logo_rect)
        screen.blit(button_play_image,button_play_image_rect)
        screen.blit(play_game_text, play_game_text_rect)
        screen.blit(button_quit_image,button_quit_image_rect)
        screen.blit(quit_text,quit_text_rect)
        

        pygame.display.update()
        