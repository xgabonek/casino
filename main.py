import time
import random
import pygame
import slot_machine as sm
import pygui

class Casino:
    def __init__(self, WIDTH, HEIGHT):
        pygame.init()
        pygame.font.init()

        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.FPS = 60   
        self.background_color = self.hex_to_rgb("#22cc22")

        self.surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
    
    def run(self):
        while True:
            self.handle_events()
            self.surface.fill(self.background_color) # bg color
            self.main_menu()
            self.clock.tick(self.FPS) # updating every 1/60 seconds
            pygame.display.flip() # updating the display

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # when pressing the close button
                exit()

    def roulette(self):
        pass

    def slot_machine(self):
        sm.main()

    def poker(self):
        pass

    def blackjack(self):
        pass

    def main_menu(self):
        button_slot_machine = pygui.Button(100, 100, 100, 100, 'Nigger', color="#ffffff")
        button_slot_machine.draw(self.surface)

    def hex_to_rgb(self, value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


if __name__ == '__main__':
    casino = Casino(800, 600)
    casino.run()