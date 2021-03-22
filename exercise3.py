winning_number=18
guessed_number=int(input("guess a number between 1 to 100:"))
if winning_number==guessed_number:
    print("you win !!!")
else:
    if winning_number>guessed_number:
        print("too low")
    else:
        print("too high")    