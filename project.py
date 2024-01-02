import random

def game():
    name = input("Your name: ")
    while True:
        try_it = 0
        points = 0
        numbers = random.randint(1, 10)
        
        pocetak = input("To start, write YES, if you want to exit, write NO: ").upper()
        if pocetak == "NO":
            print("You have exited the program.")
            break
        
        if pocetak != "YES":
            print("Please enter YES to start or NO to exit.")
            continue
        
        while True:
            try:
                unos = int(input("Try to guess the number (between 1 and 10): "))
                if unos < 1 or unos > 10:
                    print("Please enter a number between 1 and 10.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue
            
            try_it += 1
            if unos == numbers:
                points += 1
                print(f"You guessed it!\nYour name: {name}\nTry: {try_it}\nPoints: {points}")
                break
            else:
                print("Try again.")
    
if __name__ == '__main__':
    game()
