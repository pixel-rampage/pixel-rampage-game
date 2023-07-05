import pygame

pygame.joystick.init()

class Joystickclass():

    def __init__(self):
        self.joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

    ##  جير يمين  analog right    
    def joystick_run_right(self):       
        for joy in self.joysticks:
            if round(joy.get_axis(0))>0 or joy.get_hat(0)== (1,0):
                return True
            else: 
                return False 

    ## جير يسار    analog left    
    def joystick_run_left(self):       
        for joy in self.joysticks:
            if round(joy.get_axis(0))<0 or joy.get_hat(0)== (-1,0):
                return True
            else: 
                return False

    ##  جير اعلى    analog up   
    # def joystick_check_if_run_up(self):        
    #     for joy in self.joysticks:
    #         if round(joy.get_axis(1))<0 or joy.get_hat(0)== (0,1):
    #             return True
    #         else: 
    #             return False

    # ##  جير اسفل   analog down   
    # def joystick_check_if_run_down(self):         
    #     for joy in self.joysticks:
    #         if round(joy.get_axis(1))>0 or joy.get_hat(0)== (0,-1):
    #             return True
    #         else: 
    #             return False  

    ##   أكس Cross Button   
    def joystick_a_button(self):
        for joy in self.joysticks:
            if joy.get_button(0):
                return True
            else: 
                return False        
    
    ## دائرة Circle Button    
    def joystick_b_button(self):
        for joy in self.joysticks:
            if joy.get_button(1):
                return True
            else: 
                return False
                    
    ##  مربع Square Button             
    def joystick_x_button(self):
        for joy in self.joysticks:
            if joy.get_button(2):
                return True
            else: 
                return False 
            
    # ## مثلث  Triangle Button        
    # def joystick_check_if____Y__button(self):
    #     for joy in self.joysticks:
    #         if joy.get_button(3):
    #             return True
    #         else: 
    #             return False 
    ##  R1  button                     
    # def joystick_check_if____R1__button(self):
    #     for joy in self.joysticks:
    #         if joy.get_button(5):
    #             return True
    #         else: 
    #             return False
            
    # ## L1   button      
    # def joystick_check_if____L1__button(self):
    #     for joy in self.joysticks:
    #         if joy.get_button(4):
    #             return True
    #         else: 
    #             return False

    ## OPTION (menu)  button         
    def joystick_option_button(self):
        for joy in self.joysticks:
            if joy.get_button(7):
                return True
            else: 
                return False      
