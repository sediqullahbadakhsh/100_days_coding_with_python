print("Welcome to Tresure Island.\n Your mission is to find the treauser.\n")
instruction = input("Please write left or right: ")

if instruction == "left":
    instruction = input("Please write swim or wait: ")
    if instruction == "wait":
        instruction = input("Please write only color name: red, blue or yellow: ")
        if instruction =="yellow":
            print("You Win!")
        else:
            print("Game Over!")
    else:
        print("Game Over!")
    
else:
     print ("Game Over!")
