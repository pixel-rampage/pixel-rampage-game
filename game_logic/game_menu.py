import pygame

pygame.init()

class Menus:
    def __init__(self):
          self.font = pygame.font.Font("assets\\fonts\game_over.ttf",128)

    def logo_info(self,position):
        logo = self.font.render("Pixel Rampage",False,"#F5F5F5")
        logo_rect = logo.get_rect(midtop = position)
        return logo,logo_rect

    def button(self, position, img, button_text,text_color):
        text = self.font.render(button_text,True,text_color)
        button_image = pygame.image.load(img)
        button_image_rect = button_image.get_rect(center=position)
        text1_pos =(position[0], position[1]-(position[1]*0.02))
        text_rect = text.get_rect(center = text1_pos)
        return button_image,button_image_rect,text,text_rect
    
    def start_game_menu(self,buttons_path,screen_width,screen_height,text_color):
        logo,logo_rect = self.logo_info((screen_width*0.5, screen_height*0.15))
        button_play_image,button_play_image_rect,play_game_text,play_game_text_rect = self.button((screen_width*0.5, screen_height*0.45),buttons_path[0],"Play",text_color[0])
        button_quit_image,button_quit_image_rect,quit_text,quit_text_rect = self.button((screen_width * 0.5, screen_height * 0.7),buttons_path[1],"Quit",text_color[1])
        return logo, logo_rect, button_play_image, button_play_image_rect, play_game_text, play_game_text_rect, button_quit_image, button_quit_image_rect, quit_text, quit_text_rect   
        
    def pause_game_menu(self,screen_width,screen_height,text_color):
        pass  