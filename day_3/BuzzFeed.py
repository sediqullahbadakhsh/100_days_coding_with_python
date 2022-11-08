print("Wlcome to the Love Calculator")
name1 = input("What is your name? \n")
name2 = input("What is your crush name? \n")

combinedName = name1.lower() + name2.lower()

t = combinedName.count("t")
r = combinedName.count("r")
u = combinedName.count("u")
e = combinedName.count("e")

true = t+r+u+e

l = combinedName.count("l")
o = combinedName.count("o")
v = combinedName.count("v")
e = combinedName.count("e")
 
love = l+o+v+e

combinedScore = str(true) + str(love)
score = int(combinedScore)

if score <10 and score >90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif score >=40 and score <=50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")


