import pygame
import os
import pygame.mixer

pygame.init()
pygame.mixer.init()

class Sound:
    def __init__(self):
        self.Background_Level1 = pygame.mixer.Sound(r"C:\Users\doaaz\projects\pixel-rampage-game\game_logic\assets\audio\b_Level1.ogg")
        self.Background_Level2 = pygame.mixer.Sound(r"C:\Users\doaaz\projects\pixel-rampage-game\game_logic\assets\audio\bg_L2.mp3")
        self.win = pygame.mixer.Sound(r"C:\Users\doaaz\projects\pixel-rampage-game\game_logic\assets\audio\win_sound.mp3")
        self.loss = pygame.mixer.Sound(r"C:\Users\doaaz\projects\pixel-rampage-game\game_logic\assets\audio\loss_sound.wav")
        self.End_Level = pygame.mixer.Sound(r"C:\Users\doaaz\projects\pixel-rampage-game\game_logic\assets\audio\endoflevels.mp3")
        self.jump = pygame.mixer.Sound("assets\audio\Jump.mp3")
        self.Key = pygame.mixer.Sound(r"C:\Users\doaaz\projects\pixel-rampage-game\game_logic\assets\audio\Key.wav")
        self.attack =pygame.mixer.Sound (r"C:\Users\doaaz\projects\pixel-rampage-game\game_logic\assets\audio\attack.mp3")
        self.coins = pygame.mixer.Sound(r"C:\Users\doaaz\projects\pixel-rampage-game\game_logic\assets\audio\coins.mp3")
        self.select = pygame.mixer.Sound(r"C:\Users\doaaz\projects\pixel-rampage-game\game_logic\assets\audio\select.wav")
        self.resume = pygame.mixer.Sound(r"C:\Users\doaaz\projects\pixel-rampage-game\game_logic\assets\audio\resume.ogg")
#assets\audio\attack.mp3

    def play_background_level1(self):
        pygame.mixer.music.load(self.Background_Level1)
        pygame.mixer.music.play()

    def play_background_level2(self):
        pygame.mixer.music.load(self.Background_Level2)
        pygame.mixer.music.play()

    def play_win(self):
        pygame.mixer.music.load(self.win)
        pygame.mixer.music.play()

    def play_loss(self):
        pygame.mixer.music.load(self.loss)
        pygame.mixer.music.play()

    def play_end_level(self):
        pygame.mixer.music.load(self.End_Level)
        pygame.mixer.music.play()

    def play_jump(self):
        c=pygame.mixer.music.load(self.jump)
        pygame.mixer.music.play(c)

    def play_key(self):
        pygame.mixer.music.load(self.Key)
        pygame.mixer.music.play()

    def play_attack(self):
        pygame.mixer.music.load(self.attack)
        pygame.mixer.music.play()

    def play_coins(self):
        pygame.mixer.music.load(self.coins)
        pygame.mixer.music.play()

    def play_select(self):
        pygame.mixer.music.load(self.select)
        pygame.mixer.music.play()

    def play_resume(self):
        pygame.mixer.music.load(self.resume)
        pygame.mixer.music.play()

    def stop_background_level1(self):
        pygame.mixer.music.stop()

    def stop_background_level2(self):
        pygame.mixer.music.stop()

    def stop_win(self):
        pygame.mixer.music.stop()

    def stop_loss(self):
        pygame.mixer.music.stop()

    def stop_end_level(self):
        pygame.mixer.music.stop()

    def stop_jump(self):
        pygame.mixer.music.stop()

    def stop_key(self):
        pygame.mixer.music.stop()

    def stop_attack(self):
        pygame.mixer.music.stop()

    def stop_coins(self):
        pygame.mixer.music.stop()

    def stop_select(self):
        pygame.mixer.music.stop()

    def stop_resume(self):
        pygame.mixer.music.stop()
if __name__== "__main__":
    sound0 = Sound()
    sound0.play_jump()
    print("Audio")
  