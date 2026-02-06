import random

print("Welcome To Number Gussing Game:- ")

while True:
    try:
        
        user_input = int(input("Guess Number( 1 to 5):- "))
        
        ran_number = random.randint(1, 5)
        
        if user_input > ran_number:
            print("Too High Number")
        elif user_input < ran_number:
            print("Too Low Number")
        else:
            print("Congratulations You Guess Right Number")
            break
    except:
        print("Please Enter Number Only 1 to 5")
        
            