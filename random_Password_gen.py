import random
import string

while True:
    try:
        user_input = int(input("Please Enter Your Password Len:- "))
        
        if user_input <= 11:
            print("TIP:- Please Select Pass. Length 12 Dig.:- ")
        else:
            char = string.ascii_letters + string.punctuation
            
            password = "".join(random.choice(char) for len in range(user_input))
            print(f"Your Password Is :- {password}")
            agin = input("For Exit Please Enter 'y' ").lower()
            if agin == "y":
                print("thank You")
                break
    except:
        print("Program Error")
        
        