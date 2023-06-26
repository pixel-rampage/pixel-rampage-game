import pygame
import pygame.mixer
pygame.init()
pygame.mixer.init()

class Sounds:
    def __init__(self):
        self.Background_Level1=pygame.mixer.Sound("assets\audio\b_Level1.ogg")
        self.Background_Level2=pygame.mixer.Sound("assets\audio\bg_L2.mp3")
        self.win=pygame.mixer.Sound("assets\audio\win_sound.mp3")
        self.loss=pygame.mixer.Sound("assets\audio\loss_sound.wav")
        self.End_Level=pygame.mixer.Sound("assets\audio\endoflevels.mp3")
        self.jump=pygame.mixer.Sound("assets\audio\Jump.mp3")
        self.Key=pygame.mixer.Sound("assets\audio\Key.wav")
        self.attack=pygame.mixer.Sound("assets\audio\attack.mp3")
        self.coins=pygame.mixer.Sound("assets\audio\coins.wav")
        self.select=pygame.mixer.Sound("assets\audio\select_sound.mp3")
        self.resume=pygame.mixer.Sound("assets\audio\Waiting III Looped.ogg")

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume)
        for sound in self.__dict__.values():
            if isinstance(sound, pygame.mixer.Sound):
                sound.set_volume(volume)


    def play_background_level1(self, volume=1.0):
        self.background_level1.set_volume(volume)
        self.background_level1.play()

    def play_background_level2(self, volume=1.0):
        self.background_level2.set_volume(volume)
        self.background_level2.play()

    def play_win(self, volume=1.0):
        self.win.set_volume(volume)
        self.win.play()

    def play_loss(self, volume=1.0):
        self.loss.set_volume(volume)
        self.loss.play()

    def play_end_level(self, volume=1.0):
        self.end_level.set_volume(volume)
        self.end_level.play()

    def play_jump(self, volume=1.0):
        self.jump.set_volume(volume)
        self.jump.play()

    def play_key(self, volume=1.0):
        self.key.set_volume(volume)
        self.key.play()

    def play_attack(self, volume=1.0):
        self.attack.set_volume(volume)
        self.attack.play()

    def play_coins(self, volume=1.0):
        self.coins.set_volume(volume)
        self.coins.play()

    def play_select(self, volume=1.0):
        self.select.set_volume(volume)
        self.select.play()

    def play_resume(self, volume=1.0):
        self.resume.set_volume(volume)
        self.resume.play()

