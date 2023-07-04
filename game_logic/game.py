import pygame
from game_menu import StartGameMenu, PauseGameMenu, GameOverMenu
from level_maker import LevelMaker
from sys import exit

pygame.init()

def quit_game():
    pygame.quit()
    exit()

#this function to get the position for level one
def ground_list(ground_type,screen_height):
    image1 = pygame.image.load(ground_type[0]).convert_alpha()
    ground_width = image1.get_width()
    ground_height = image1.get_height()-20
    del image1
    ground1_position = []
    for i in range(3):
        ground1_position.append((ground_width * i, screen_height+20))
    pos_list = [(1300, screen_height-150), (1820, screen_height-320),
                ((ground_width * 10)+20, screen_height-220)]
    for element in pos_list:
        ground1_position.append(element)
    for i in range(11, 13):
        ground1_position.append((ground_width * i, screen_height+20))
    pos_list = [((ground_width * 13)+70, screen_height-150),
                ((ground_width * 15)-50, screen_height-150)]
    for element in pos_list:
        ground1_position.append(element)
    for i in range(16, 20):
        ground1_position.append((ground_width * i, screen_height+20))
    ground1_position.append(((ground_width * 2)+50, screen_height-340))
    ground3_position = [((ground_width * 16)+100, screen_height-350),
                        ((ground_width * 17)+100, screen_height-350),
                        ((ground_width * 18)+100, screen_height-350)
                        ]
    ground4_position = [((ground_width * 18)+500, screen_height-300),
                        ((ground_width * 18)+800, screen_height-450),
                        ((ground_width * 18)+1100, screen_height-450)
                        ]
    return ground1_position,ground3_position,ground4_position,ground_height


# this is the main function
def main():
    # building the screen
    pygame.display.set_caption("Pixel Rampage")
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    FPS = 60

    #creating some needed variable for the game to run
    game_over_sound = pygame.mixer.Sound("assets\\audio\\loss_sound.wav")
    game_state = "start_game"
    pause_or_not = False
    background_type = "assets\\backgrounds\\game_background\\sky_"
    ground_type = [
        "assets\\grounds\\ground1.png",
        "assets\\grounds\\ground2.png",
        "assets\\grounds\\ground3.png",
        "assets\\grounds\\ground4.png"
    ]
    background_object_list = [
        "assets\\game_objects\\tree.png",
        "assets\\game_objects\\door_off.png",
        "assets\\game_objects\\door_on.png",
    ]
    ground1_position,ground3_position,ground4_position,ground_height = ground_list(ground_type,screen_height)
    tree_position = (250,screen_height-ground_height)
    door_position = (max(ground1_position, key=lambda x: x[0])[0],screen_height - ground_height)

    #making the object
    start_game = StartGameMenu(screen_width, screen_height)
    pause_game = PauseGameMenu(screen_width, screen_height)
    game_over = GameOverMenu(screen_width, screen_height)
    level_one = LevelMaker(screen_width, screen_height, background_type)
    for ground in ground1_position:
        level_one.add_ground(ground_type[0], ground)
    level_one.add_ground(ground_type[1], (2730, screen_height+600))
    for ground in ground3_position:
        level_one.add_ground(ground_type[2], ground)
    for ground in ground4_position:
        level_one.add_ground(ground_type[3], ground)
    level_one.add_level_object(background_object_list[0],tree_position)
    level_one.add_level_object(background_object_list[1],door_position)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if game_state == "start_game":
                start_game.buttons[0].hover()
                start_game.buttons[1].hover()
                if start_game.buttons[0].button_clicked(event):
                    pygame.mouse.set_visible(False)
                    game_state = "playing"
                if start_game.buttons[1].button_clicked(event):
                    quit_game()
            elif game_state == "playing":

                # puase menu events handler
                if event.type == pygame.KEYDOWN and not pause_or_not:
                    if event.key == pygame.K_ESCAPE:
                        pause_or_not = True
                        pygame.mouse.set_visible(True)
                    if event.key == pygame.K_1:
                        pygame.mouse.set_visible(True)
                        game_over_sound.play()
                        # level_one.level_reset()
                        game_state = "game_over"

                if pause_or_not:
                    pause_game.buttons[0].hover()
                    pause_game.buttons[1].hover()
                    if pause_game.buttons[0].button_clicked(event):
                        pygame.mouse.set_visible(False)
                        pause_or_not = False
                    if pause_game.buttons[1].button_clicked(event):
                        level_one.level_reset()
                        pause_or_not = False
                        game_state = "start_game"
            
            if game_state == "game_over":
                game_over.buttons[0].hover()
                game_over.buttons[1].hover()
                if game_over.buttons[0].button_clicked(event):
                    level_one.level_reset()
                    pygame.mouse.set_visible(False)
                    game_over_sound.stop()
                    game_state = "playing"
                if game_over.buttons[1].button_clicked(event):
                    level_one.level_reset()
                    game_over_sound.stop()
                    game_state = "start_game"
            

        if game_state == "start_game":
            start_game.start_game_draw(screen)
        elif game_state == "playing":
            if pause_or_not:
                pause_game.pause_game_draw(screen)
            else:
                # all the draws here
                level_one.draw(screen)

                # all the update here
                level_one.update_position()

            
        elif game_state == "game_over":
            game_over.game_over_draw(screen)

            
        frame_rate = clock.get_fps()
        print(frame_rate)
        clock.tick(FPS)
        pygame.display.update()


if __name__ == "__main__":
    main()
