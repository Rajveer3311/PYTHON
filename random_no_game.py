import random
winning_number=random.randint(1,100)
guess=1
number=int(input("guess a number b/w 1 to 100:"))
game_over=False
while True://while not guess_over
    if winning_number==number:
        print(f"you win !!! you guessed this number {guess} times.")
        break //guess_over=True
    else:
        if number<winning_number:
            print("Too low")
        else:
            print("Too high")  

        guess+=1
        number=int(input("guess again:")) 