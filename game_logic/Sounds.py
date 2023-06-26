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
        self.Background_Level1.set_volume(volume)
        self.Background_Level1.play()

    def play_background_level2(self, volume=1.0):
        self.Background_Level2.set_volume(volume)
        self.Background_Level2.play()

    def play_win(self, volume=1.0):
        self.win.set_volume(volume)
        self.win.play()

    def play_loss(self, volume=1.0):
        self.loss.set_volume(volume)
        self.loss.play()

    def play_end_level(self, volume=1.0):
        self.End_Level.set_volume(volume)
        self.End_Level.play()

    def play_jump(self, volume=1.0):
        self.jump.set_volume(volume)
        self.jump.play()

    def play_key(self, volume=1.0):
        self.Key.set_volume(volume)
        self.Key.play()

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

    def stop_background_level1(self):
        self.Background_Level1.stop()

    def stop_background_level2(self):
        self.Background_Level2.stop()

    def stop_win(self):
        self.win.stop()

    def stop_loss(self):
        self.loss.stop()

    def stop_end_level(self):
        self.End_Level.stop()

    def stop_jump(self):
        self.jump.stop()

    def stop_key(self):
        self.Key.stop()

    def stop_attack(self):
        self.attack.stop()

    def stop_coins(self):
        self.coins.stop()

    def stop_select(self):
        self.select.stop()

    def stop_resume(self):
        self.resume.stop()
