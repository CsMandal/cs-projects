import random
answer=random.randint(0,100)
game_end=False
def gameplay(attempt):
    for i in range(attempt):
        print(f"\nYou have remaining {attempt - i} attempts Guess again  ")
        guess_no=int(input("Guess a no. : "))
        if guess_no==answer:
            return f"You Win !! number was {answer}"
        elif guess_no>answer:
            print("Too high!!!")
        else:
            print("Too low!!!")

    return "You loose !!!"

print(f"Welcome to the guess a number ".title())
print("choose the nuber in 0 - 100")
level=input("Choose the level easy-10attempts hard-5attempts").lower()
if level=='easy':
    message=gameplay(10)
elif level=='hard':
    message=gameplay(5)
else:
    print("INVALID CHOICE")
print(message)