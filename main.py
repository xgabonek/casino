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
        self.FPS = 240  
        self.background_color = self.hex_to_rgb("#73615a")

        self.user_playing = user_playing
        self.bet = 0

        self.surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()

        self.slots = None
        self.slot_animation = None
        self.slot_color = "#fff"
        self.symbols = ['🍒', '🍉', '🍎', '🍊', '⭐']
        self.message_label = pygui.Label((self.WIDTH // 2 - 200, self.HEIGHT - 300), 400, 50, "!!  SPIN  !!")

        self.current_window = 0 # 0 - Main menu; 1 - Roulette; 2 - Slot machine; 3 - Poker; 4 - Blackjack
    
    def gain(self, *args):
        self.user_playing.balance += 1

    def run(self):
        while True:
            self.handle_events()
            self.surface.fill(self.background_color) # bg color

            # common for all windows
            label_balance = pygui.Label((10, 10), 100, 50, f'Balance: {self.user_playing.balance}', background_color='##383230', font_size=20)
            label_balance.draw(self.surface)

            button_gain = pygui.Button(label_balance, 50, 50, "+", font_size=42, func=self.gain, stick_or_insert=0)
            button_gain.draw(self.surface)

            label_text = pygui.Label((self.WIDTH // 2 - 100, 10), 200, 100, 'CASINEGRO', background_color='#383230', font_size=40)
            label_text.draw(self.surface)

            button_minusminus = pygui.Button((10, self.HEIGHT - 60), 50, 50, "--", func=self.change_bet, args=[-25], font_size=40)
            button_minusminus.draw(self.surface)

            button_minus = pygui.Button(button_minusminus, 50, 50, "-", func=self.change_bet, args=[-5], font_size=40, stick_or_insert=0)
            button_minus.draw(self.surface)

            bet_label = pygui.Label(button_minus, 80, 50, f"Bet: {self.bet}", font_size=28, stick_or_insert=0)
            bet_label.draw(self.surface)

            button_plus = pygui.Button(bet_label, 50, 50, "+", func=self.change_bet, args=[5], font_size=40, stick_or_insert=0)
            button_plus.draw(self.surface)

            button_plusplus = pygui.Button(button_plus, 50, 50, "++", func=self.change_bet, args=[25], font_size=40, stick_or_insert=0)
            button_plusplus.draw(self.surface)

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

    def animate_slot_machine(self, row, result, win):
        self.message_label.change_text("SPINING...")
        for i in range(15):
            for slot in self.slots: 
                slot.change_text(random.choice(self.symbols))
            time.sleep(0.05 * (i // 2))
        for j, slot in enumerate(self.slots):
            slot.change_text(row[j])
        self.user_playing.balance += win
        if result:
            self.message_label.change_text("You won!!")
            for i in range(5):
                self.slot_color = "#f5d142"
                time.sleep(0.1)
                self.slot_color = "#383230"
                time.sleep(0.1)
        else:
            self.message_label.change_text("You lose XDD")
            for i in range(5):
                self.slot_color = "#77ff00"
                time.sleep(0.1)
                self.slot_color = "#383230"
                time.sleep(0.1)
        self.message_label.change_text("!!  SPIN  !!")


    def spin_slot_machine(self, arg):
        slots = SlotMachine()
        if 0 < self.bet <= self.user_playing.balance and (not self.slot_animation or not self.slot_animation.is_alive()):
            self.user_playing.balance -= self.bet
            result, row, win = slots.spin(self.bet)
            butthole = 0
            self.slot_animation = threading.Thread(target=self.animate_slot_machine, args=[row, result, win], daemon=True)
            self.slot_animation.start()

    def slot_machine(self):
        # SLOTS
        back_label = pygui.Label((self.WIDTH // 2 - self.WIDTH // 4 - 10, self.HEIGHT // 4 - 10), self.WIDTH // 2 + 20, self.HEIGHT // 3 + 20, text="", background_color=self.slot_color)
        back_label.draw(self.surface)
        if self.slots is None:
            cell_width = self.WIDTH // 6
            self.slots = [
                pygui.Label(back_label, self.WIDTH // 6, self.HEIGHT // 3, text="-", background_color="#383230", color="#333", font_size=50, stick_or_insert=1),
            ]
            self.slots.append(pygui.Label(self.slots[0], self.WIDTH // 6, self.HEIGHT // 3, text="-",      background_color="#383230", color="#333", font_size=50, stick_or_insert=0, margin=[0, 0]))
            self.slots.append(pygui.Label(self.slots[1], self.WIDTH // 6, self.HEIGHT // 3, text="-",      background_color="#383230", color="#333", font_size=50, stick_or_insert=0, margin=[0, 0]))

        for slot in self.slots:
            slot.draw(self.surface)

        slot_button = pygui.Button((self.WIDTH / 2 - 50, self.HEIGHT // 5 * 4), 100, 50, 'SPIN', font_size=30, func=self.spin_slot_machine)
        slot_button.draw(self.surface)

        autospin_checkbox = pygui.Checkbox(slot_button, 50, False, stick_or_insert=0)
        autospin_checkbox.draw(self.surface)

        self.message_label.draw(self.surface)


    def poker(self):
        pass

    def blackjack(self):
        pass

    def main_menu(self):
        button_slot_machine = pygui.Button((100, self.HEIGHT//2 - 50), 
                                           width=200, height=100, text='Slot machine', background_color="#fff", color="#383230", 
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
        self.balance = 1000000000000000000000

if __name__ == '__main__':
    player = Account('joumey')
    casino = Casino(1200, 800, player)
    casino.run()