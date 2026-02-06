while True:
    try:
        print("For Exit Type 0")
        num1 = int(input("Please Enter Your 1st No:- "))
        
        if num1 == 0:
            break
        num2 = int(input("Please Enter Your 2nd No:- "))
        op = input("Please Enter Your Op(+,-,/,x):- ")
        
        
        if op == "+":
            r = num1 + num2
            print("Your Sum:- ", r)
        elif op == "-":
            r = num1 - num2
            print("Your Diff:- ", r)
        elif op == "*":
            r = num1 * num2
            print("Your Multy:- ", r)
        elif op == "/":
            if num2 == 0:
                print (ZeroDivisionError)
            else:
                r = num1 / num2
                print("Your Divd:- ", r)
        else:
            print("Enter Valid Entry")
    except ValueError:
        print("Error")