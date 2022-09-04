import random
from art import logo
print(logo)
print("Welcome to the number Guessing Game")
print("Think a number between 1 to 100 ")
user_choice=int(input("choose a difficulty . Type 0 for Easy, Type 1 for hard \n"))
if user_choice==0:
    num=random.randint(0,100)

    print("You Have 10 attempts remaining to Guess a number")
    for i in range(10):
        
        guess_number=int(input("make a guess: "))
        if num==guess_number:
            print(f"you got it! answer was {num} ")
        if num>guess_number:
            print("Too low ")
            print(f"you used {i} attempt out of 10 ")
        if num<guess_number:
            print("Too High")
            print(f"you used {i} attempt out of 10 ")

elif user_choice==1:
    num=random.randint(0,100)
    print("You Have 5 attempts remaining to Guess a number")
    for i in range(5):
        guess_number=int(input("make a guess: "))
        if num==guess_number:
            print(f"you got it! answer was {num} ")
        if num>guess_number:
            print("Too low ")
            print(f"you used {i} attempt out of 5 ")
        if num<guess_number:
            print("Too High")
            print(f"you used {i} attempt out of 5 ")
else:
    print("invalid guess")

    


    








