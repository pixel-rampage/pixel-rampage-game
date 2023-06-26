import pygame
import os
import pygame.mixer

pygame.init()
pygame.mixer.init()

class Sound:
    def __init__(self):
        self.Background_Level1 = os.path.join("assets","audio", "b_Level1.ogg")
        self.Background_Level2 = os.path.join("assets","audio", "bg_L2.mp3")
        self.win = os.path.join("assets","audio", "win_sound.mp3")
        self.loss = os.path.join("assets","audio", "loss_sound.wav")
        self.End_Level = os.path.join("assets","audio", "endoflevels.mp3")
        self.jump = os.path.join("assets","audio", "Jump.mp3")
        self.Key = os.path.join("assets","audio", "Key.wav")
        self.attack =os.path.join ("assets","audio", "attack.mp3")
        self.coins = os.path.join("assets","audio", "coins.mp3")
        self.select = os.path.join("assets","audio", "select_sound.mp3")
        self.resume = os.path.join("assets","audio", "Waiting III Looped.ogg")
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
        pygame.mixer.music.load(self.jump)
        pygame.mixer.music.play()

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
    sound0.play_loss()
    print("Audio")
