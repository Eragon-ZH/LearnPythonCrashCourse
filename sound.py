import pygame.mixer

class Music():

    def __init__(self):
        pygame.mixer.init()
        # pygame.mixer.set_number_channels(2)
        self.bg_music = pygame.mixer.Sound("./music/main.wav")
        self.biu_music = pygame.mixer.Sound("./music/biu.wav")
