import random


def game():
    name = input("Your name: ")
    try_it = 0
    points = 0
    numbers = random.randint(1,10)
    while True:
        try:
            pocetak = input("To start, write YES, if you don't want NO: ")
        except:
            print("Please follow the instructions")
        while pocetak == "YES":
            try:
                unos = int(input("Try to guess the number: "))
            except:
                print("Uenter a number from 1 to 10")
            if unos>10 or unos < 1:
                print("You cannot enter those numbers")
            if unos == numbers:
                try_it+=1
                points +=1
                print(f"You guessed it.\nYour name: {name}\nTry: {try_it}\nPoints: {points}")
                break
            elif unos!=numbers:
                try_it+=1
            else:
                print("Try again.")
        if pocetak == "NO":
            print("You have exited the program.")
            break
        


if __name__ == '__main__':
    game()