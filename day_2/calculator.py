# num_char = len(input("Type your name: "))
# print (type(num_char))

# type converstion
# str("statment") to convert number into string
# float("statement") to convert to float
# int("statement") to convert to Integer

# print(type(int("123")))

# a = "123"
# n = int(a)
# b = 1.23
# c = int(a) + 34
# print(c)
# #print (a + " + " + str(b) + " = " + str(c))

# rount(float number, decimal places)

score = 0
height = 1.8
isWinning = False
#f-String
#print(f"your score is {score}, your height is {height}, and your winning is {isWinning}")

### Tipe calculator
print ("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10,20,30? "))
people = int(input("How may people to split the bill?"))
bill_with_tip = round(bill * (1 + tip/100),2)
# or tip / 100 * bill + bill
print (f"each personle should pay {bill_with_tip}")