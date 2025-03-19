import time
import random
import pygame
import pygui
from slot_machine import SlotMachine
import threading

class Casino:
    def __init__(self, WIDTH, HEIGHT, user_playing):
        pygame.init()
        pygame.font.init()

        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.FPS = 60   
        self.background_color = self.hex_to_rgb("#a1eb34")

        self.user_playing = user_playing
        self.bet = 0

        self.surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()

        cell_width = self.WIDTH // 6
        self.slots = [
            pygui.Label((self.WIDTH // 2 - cell_width - cell_width // 2, self.HEIGHT // 4), self.WIDTH // 6, self.HEIGHT // 3, text="-", background_color="#ccc", color="#333", font_size=50),
            pygui.Label((self.WIDTH // 2 - cell_width - cell_width // 2 + cell_width, self.HEIGHT // 4), self.WIDTH // 6, self.HEIGHT // 3, text="-", background_color="#ccc", color="#333", font_size=50),
            pygui.Label((self.WIDTH // 2 - cell_width - cell_width // 2 + cell_width * 2, self.HEIGHT // 4), self.WIDTH // 6, self.HEIGHT // 3, text="-", background_color="#ccc", color="#333", font_size=50),
        ]
        self.slot_animation = None
        self.slot_color = self.hex_to_rgb("#5c5")
        self.symbols = ['🍒', '🍉', '🍎', '🍊', '⭐']
        self.message_label = pygui.Label((self.WIDTH // 2 - 200, self.HEIGHT - 300), 400, 50, "!!  SPIN  !!")

        self.current_window = 0 # 0 - Main menu; 1 - Roulette; 2 - Slot machine; 3 - Poker; 4 - Blackjack
    
    def run(self):
        while True:
            self.handle_events()
            self.surface.fill(self.background_color) # bg color

            # common for all windows
            label_balance = pygui.Label((10, 10), 100, 50, f'Balance: {self.user_playing.balance}', background_color='#a1eb34', font_size=20)
            label_balance.draw(self.surface)

            label_text = pygui.Label((self.WIDTH // 2 - 100, 10), 200, 100, 'CASINEGRO', background_color='#a1eb34', font_size=40)
            label_text.draw(self.surface)

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

    def animate_slot_machine(self, row, result):
        self.message_label.change_text("SPINING...")
        for i in range(15):
            for slot in self.slots: 
                slot.change_text(random.choice(self.symbols))
            time.sleep(0.05 * (i // 2))
        for j, slot in enumerate(self.slots):
            slot.change_text(row[j])
            
        if result:
            self.message_label.change_text("You won!!")
            for i in range(5):
                self.slot_color = self.hex_to_rgb("#f5d142")
                time.sleep(0.1)
                self.slot_color = self.hex_to_rgb("#5c5")
                time.sleep(0.1)
        else:
            self.message_label.change_text("You lose XDD")
            for i in range(5):
                self.slot_color = self.hex_to_rgb("#f55742")
                time.sleep(0.1)
                self.slot_color = self.hex_to_rgb("#5c5")
                time.sleep(0.1)
        self.message_label.change_text("!!  SPIN  !!")


    def spin_slot_machine(self, arg):
        slots = SlotMachine()
        if 0 < self.bet <= self.user_playing.balance and (not self.slot_animation or not self.slot_animation.is_alive()):
            self.user_playing.balance -= self.bet
            result, row, win = slots.spin(self.bet)
            self.user_playing.balance += win
            butthole = 0
            self.slot_animation = threading.Thread(target=self.animate_slot_machine, args=[row, result], daemon=True)
            self.slot_animation.start()

    def slot_machine(self):
        # SLOTS
        pygame.draw.rect(self.surface, self.slot_color, (self.WIDTH // 2 - self.WIDTH // 4 - 10, self.HEIGHT // 4 - 10, self.WIDTH // 2 + 20, self.HEIGHT // 3 + 20))

        for slot in self.slots:
            slot.draw(self.surface)

        slot_button = pygui.Button((self.WIDTH / 2 - 50, self.HEIGHT // 5 * 4), 100, 50, 'SPIN', font_size=30, func=self.spin_slot_machine)
        slot_button.draw(self.surface)

        button_minus = pygui.Button((10, self.HEIGHT - 60), 50, 50, "--", func=self.change_bet, args=[-25], font_size=40)
        button_minus.draw(self.surface)

        button_minus = pygui.Button((70, self.HEIGHT - 60), 50, 50, "-", func=self.change_bet, args=[-5], font_size=40)
        button_minus.draw(self.surface)

        bet_label = pygui.Label((130, self.HEIGHT - 60), 120, 50, f"Bet: {self.bet}", font_size=28)
        bet_label.draw(self.surface)
        
        button_plus = pygui.Button((260, self.HEIGHT - 60), 50, 50, "+", func=self.change_bet, args=[5], font_size=40)
        button_plus.draw(self.surface)
        
        button_plusplus = pygui.Button((320, self.HEIGHT - 60), 50, 50, "++", func=self.change_bet, args=[25], font_size=40)
        button_plusplus.draw(self.surface)

        self.message_label.draw(self.surface)


    def poker(self):
        pass

    def blackjack(self):
        pass

    def main_menu(self):
        button_slot_machine = pygui.Button(pos=(100, self.HEIGHT//2 - 50), 
                                           width=200, height=100, text='Slot machine', background_color="#509c00", color="#333", 
                                           font_size=30,
                                           func=self.change_window, args=[2])
        button_slot_machine.draw(self.surface)

    def change_window(self, window):
        self.current_window = window[0]

    def change_bet(self, diff):
        diff = diff[0]
        if diff > 0 and self.bet + diff <= self.user_playing.balance:
            self.bet += diff
        if diff < 0 and self.bet + diff > diff:
            self.bet += diff


    def hex_to_rgb(self, value): # This function makes a RGB value from HEX; example: "#fff" will return (255, 255, 255) tuple
        value = value.lstrip('#')
        if len(value) == 3:
            value = ''.join([i * 2 for i in value])
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

class Account:
    def __init__(self, username):
        self.username = username
        self.balance = 1000

if __name__ == '__main__':
    player = Account('joumey')
    casino = Casino(1200, 800, player)
    casino.run()