import random

class SlotMachine:
    def __init__(self):
        self.symbols = ['🍒', '🍉', '🍎', '🍊', '⭐']

    def spin(self, bet):
        spin_result = [random.choice(self.symbols) for i in range(3)]
        result = False
        win = 0
        if len(set(spin_result)) == 1:
            result = True
            win = bet * (self.symbols.index(spin_result[0]) + 2)
        return result, spin_result, win