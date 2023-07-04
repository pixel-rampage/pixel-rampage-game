import pygame
import sys
pygame.init()


# start menu class
class StartGameMenu:
    def __init__(self,screen_width,screen_height):
          self.font = pygame.font.Font("assets\\fonts\game_over.ttf",128)
          self.play_button = Button("Play",(screen_width*0.5, screen_height*0.45),)
          self.quit_button = Button("Quit",(screen_width * 0.5, screen_height * 0.7))
          self.screen_width = screen_width
          self.screen_height = screen_height

    def logo_info(self,position):
        logo = self.font.render("Pixel Rampage",False,"#F5F5F5")
        logo_rect = logo.get_rect(midtop = position)
        return logo,logo_rect
    
    def start_game_draw(self,screen):
        logo,logo_rect = self.logo_info((self.screen_width*0.5, self.screen_height*0.15))
        screen.blit(logo,logo_rect)
        self.play_button.draw(screen)
        self.quit_button.draw(screen)

# start menu class
class Button:
    def __init__(self,button_text, position):
        self.font = pygame.font.Font("assets\\fonts\game_over.ttf",128)
        self.button_text = button_text
        self.button_image = pygame.image.load("assets\\menu_assets\\button_off.png")
        self.text = self.font.render(button_text,True,"#F5F5F5")
        self.button_rect = self.button_image.get_rect(center=position)
        text1_pos =(position[0], position[1]-(position[1]*0.02))
        self.text_rect = self.text.get_rect(center = text1_pos)

    def hover(self):
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            self.button_image = pygame.image.load("assets\\menu_assets\\button_on.png") 
            self.text = self.font.render(self.button_text,False,"#CD7F32")
        else:
            self.button_image = pygame.image.load("assets\\menu_assets\\button_off.png")
            self.text = self.font.render(self.button_text,False,"#F5F5F5")
    
    def button_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos) and event.button == 1:
                return True
            else:
                return False

    def draw(self,screen):
        screen.blit(self.button_image,self.button_rect)
        screen.blit(self.text,self.text_rect)

# write puase menu here
class Pause:
    def __init__(self,screen_width,screen_height):
            self.font = pygame.font.Font("assets\\fonts\game_over.ttf",128)
            self.backgroung_imag=pygame.image.load('assets\menu_assets\pause_menu.png')
            self.background_rect = self.backgroung_imag.get_rect(center =(screen_width*0.5 , screen_height*0.48))
            self.pause_button = Button("Resume",(screen_width*0.5, screen_height*0.45),)
            self.quit_button = Button("Quit",(screen_width * 0.5, screen_height * 0.7))
        
            self.screen_width = screen_width
            self.screen_height = screen_height

    def logo_info(self,position):
            logo = self.font.render("Pause Game",False,"#F5F5F5")
            logo_rect = logo.get_rect(midtop = position)
            return logo,logo_rect          

    def start_game_draw(self,screen):
            logo,logo_rect = self.logo_info((self.screen_width*0.5, self.screen_height*0.15))
            width,height = self.backgroung_imag.get_size() 
            self.backgroung_imag = pygame.transform.scale(self.backgroung_imag,(width,self.screen_height*0.6))
            screen.blit(self.backgroung_imag,self.background_rect)
            screen.blit(logo,logo_rect)
            self.pause_button.draw(screen)
            self.quit_button.draw(screen)



class GameOver:
    def __init__(self, screen_width, screen_height) -> None:
        self.gameover_imag=pygame.image.load('assets\menu_assets\pause_menu.png')
        self.screen_width = screen_width
        self.screen_height = screen_height

     



    def game_over(self, screen):
        game_over_font = pygame.font.Font("assets\\fonts\game_over.ttf",128)
        game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
        screen.blit(game_over_text, (250, 250)) 



#############################################################

def quit_game():
    pygame.quit()
    exit()
        
# this is the main function
def main():
    pygame.display.set_caption("Pixel Rampage")
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width,screen_height))
    start_game_menu = StartGameMenu(screen_width, screen_height)
    game_state = "start_game"
    pause_or_not = False
    pause_menu=Pause(screen_width,screen_height)

    
    running = True
    game_over_flag = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running =False
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
                if event.type == pygame.KEYDOWN:
                        if event.key ==pygame.K_ESCAPE:
                                pause_or_not = True
                if pause_menu.pause_button.button_clicked(event):
                     pause_or_not = False
                if pause_menu.quit_button.button_clicked(event):
                          pause_or_not = False 
                          game_state = "start_game" 

                   
                


            
                #######################################################

                
        if game_state == "start_game":
            screen.fill((0, 0, 0))
            start_game_menu.start_game_draw(screen)
        elif game_state == "playing":
            screen.fill((0, 0, 0)) #this line here is to fill the screen with black
            # puase menu draw
            if pause_or_not :
                 pause_menu.pause_button.hover()
                 pause_menu.quit_button.hover()
                 pause_menu.start_game_draw(screen)
                 
                 

        

            ######################################################


        pygame.display.update()

if __name__ == "__main__":
    main()







# def draw_game_over_screen():
#    screen.fill((0, 0, 0))
#    font = pygame.font.SysFont('arial', 40)
#    title = font.render('Game Over', True, (255, 255, 255))
#    restart_button = font.render('R - Restart', True, (255, 255, 255))
#    quit_button = font.render('Q - Quit', True, (255, 255, 255))
#    screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/3))
#    screen.blit(restart_button, (screen_width/2 - restart_button.get_width()/2, screen_height/1.9 + restart_button.get_height()))
#    screen.blit(quit_button, (screen_width/2 - quit_button.get_width()/2, screen_height/2 + quit_button.get_height()/2))
#    pygame.display.update()





#    while True: 

#    for event in pygame.event.get(): 
#        if event.type == pygame.QUIT:
#            pygame.quit()
#            quit()

#         if game_state == "game_over":
#             keys = pygame.key.get_pressed()
#             if keys[pygame.K_r]:
#                 game_state = "start_menu"
#             if keys[pygame.K_q]:
#                 pygame.quit()
#                 quit()
   