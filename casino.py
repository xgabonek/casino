import time
import random
import slot_machine as sm


def roulette():
    pass

def slot_machine():
    sm.main()
def poker():
    pass

def blackjack():
    pass

def main():
    while True:
        print("----------------")
        print("Witaj w kasynie!")
        print("----------------")
        print()
        print("--------------------------------------------------------------------------------------")
        print("Dostępne gry: \n1 - Ruletka \n2 - Slot Machine \n3 - Poker \n4 - Blackjack \n0 - Wyjdź")
        print("--------------------------------------------------------------------------------------")

        wybor = input("Wybierz grę (1-4): ")
        if not wybor.isdigit():
            print("Podaj liczbę.")
            continue
        
        wybor = int(wybor)

        if wybor > 4:
            print("Nieprawidłowa liczba.")
            continue
        if wybor < 0:
            print("Nieprawidłowa liczba")
            continue
        
        match wybor:
            case 1:
                roulette()
            case 2:
                slot_machine()
            case 3:
                poker()
            case 4:
                blackjack()
            case 0:
                print("Wychodzę...")
                time.sleep(1)
                break
if __name__ == '__main__':
    main()