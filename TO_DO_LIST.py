data = []

def show_list():
    if not data:
        print("No Data Avelabile")
    else:
        print("---Your List---")
        for index, taks in enumerate(data, start=1):
            print(f"{index}: {taks.strip()}")

def add_tasks():
    new_data = input("Please Enter New task:- \n")
    data.append(new_data)
    print("Data Added")
    show_list()
    
def dalete_tasks():
    
    show_list()
    if not data:
        print("No Data Aveliable")
    else:
        new_data = int(input("Please Enter Task Number:- "))
        if 0 < new_data <= len(data):
            removedata = data.pop(new_data - 1)
            print(f"Data Deleted Done {removedata}")
        show_list()

while True:
    try:
        print("---Wellcome To TODO LIST----")
        print("1:- Show List\n2:- Add Taks\n3:- Dalete Task\n4:- Exit")
        user_input = int(input("Please Enter Your Choises:- "))
        if user_input == 4:
            break
        elif user_input == 1:
            show_list()
        elif user_input == 2:
            add_tasks()
        elif user_input == 3:
            dalete_tasks()
    except:
        print("Please Enter Valid Data")