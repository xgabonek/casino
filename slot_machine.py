import random
import time

def spin_row():
    symbole = ['🍒', '🍉', '🍎', '🍊', '⭐']

    return [random.choice(symbole) for _ in range(3)]

def get_wyplata(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍎':
            return bet * 5
        elif row[0] == '🍊':
            return bet * 7
        elif row[0] == '⭐':
            return bet * 10
    return 0

def main():
    balans = 100
    while balans > 0:
        print(f"Twój balans: {balans}zł.")

        bet = input("Ile chcesz postawić: ")

        if not bet.isdigit():
            print("Proszę wpisać numer.")
            continue
       
        bet = int(bet)

        if bet > balans:
            print("Nie możesz postawić tej kwoty.")
            continue
        
        if bet <= 0:
            print("Nie możesz postawić tej kwoty.")
            continue
        
        balans -= bet

        row = spin_row()
        print("Kręcenie...\n")
        time.sleep(1)
        print_row(row)

        wyplata = get_wyplata(row, bet)

        if wyplata > 0:
            print(f"Wygrałeś {wyplata}zł!")
        else:
            print("Przegrałeś!")

        balans += wyplata

        zagraj_ponownie = input("Czy chcesz zagrać ponownie? (T/N): ").upper()

        if zagraj_ponownie == 'N':
            break

    print("-----------------------------------------------")
    print(f"Zakończono! Twój końcowy balans to: {balans}. ")
    print("-----------------------------------------------")

if __name__ == '__main__':
    main()