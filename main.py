import time
import random
import pygame
import slot_machine as sm
import pygui

class Casino:
    def __init__(self, WIDTH, HEIGHT, user_playing):
        pygame.init()
        pygame.font.init()

        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.FPS = 60   
        self.background_color = self.hex_to_rgb("#a1eb34")

        self.user_playing = user_playing

        self.surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()

        self.current_window = 0 # 0 - Main menu; 1 - Roulette; 2 - Slot machine; 3 - Poker; 4 - Blackjack
    
    def run(self):
        while True:
            self.handle_events()
            self.surface.fill(self.background_color) # bg color
            match self.current_window:
                case 0:
                    self.main_menu()
                case 1:
                    self.roulette()
                case 2:
                    self.slot_machine()
                case 3:
                    self.poker()
                case 4:
                    self.blackjack()

            self.clock.tick(self.FPS) # updating every 1/60 seconds
            pygame.display.flip() # updating the display

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # when pressing the close button
                exit()

    def roulette(self):
        pass

    def slot_machine(self):
        

    def poker(self):
        pass

    def blackjack(self):
        pass

    def main_menu(self):
        button_slot_machine = pygui.Button(pos=(100, self.HEIGHT//2 - 50), 
                                           width=200, height=100, text='Slot machine', background_color="#509c00", color="#333", 
                                           font='Comic sans', font_size=30,
                                           function=self.change_window, args=[2])
        button_slot_machine.draw(self.surface)

    def change_window(self, window):
        self.current_window = window

    def hex_to_rgb(self, value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

class Account:
    def __init__(self, username):
        self.username = username
        self.balance = 1000

if __name__ == '__main__':
    player = Account('joumey')
    casino = Casino(800, 600, player)
    casino.run()