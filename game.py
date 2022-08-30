from gamedata import data
import random

for i in data:
    vogals = ['A', 'E', 'I', 'O', 'U']
    if i['profession'][0] in vogals:
        summary = "{} is an {} from {}".format(i['name'], i['profession'], i['country'])
    else:
        summary = "{} is a {} from {}".format(i['name'], i['profession'], i['country'])


list_continue = []

def highorlower():
    A = random.choice(data)
    B = random.choice(data)
    question = "Who has the most instagram followers: A: {} or B: {}?".format(A["name"], B["name"])
    awinner = "{} has {}m followers, more than {}, who has {}m followers".format(A["name"], A["follower_counter"], B["name"], B["follower_counter"])
    bwinner = "{} has {}m followers, more than {}, who has {}m followers".format(B["name"], B["follower_counter"], A["name"], A["follower_counter"])
    i = 0
    print(question)
    userchoice = input("Type A or B: ").upper()
    if A["follower_counter"] > B["follower_counter"]:
        if userchoice == "A":
            i = 1
            print("You're right. Keep it going")
            print(awinner)
            list_continue.append(A)
            print(list_continue)
            continuegame()
        else:
            print("You're wrong. Try again.")
            print(awinner)
    else:
        if userchoice == "B":
            i = 1
            print("You're right. Keep it going")
            list_continue.append(B)
            print(list_continue)
            print(bwinner)
            continuegame()

def continuegame():
    l = 0
    A = list_continue[l]
    B = random.choice(data)
    question = "Who has the most instagram followers: A: {} or B: {}?".format(A["name"], B["name"])
    awinner = "{} has {}m followers, more than {}, who has {}m followers".format(A["name"], A["follower_counter"], B["name"], B["follower_counter"])
    bwinner = "{} has {}m followers, more than {}, who has {}m followers".format(B["name"], B["follower_counter"], A["name"], A["follower_counter"])
    i = 1
    print(question)
    userchoice = input("Type A or B: ").upper()
    while True:
        if userchoice == "A":
            if A["follower_counter"] > B["follower_counter"]:
                i += 1
                l +=1
                print("You're right. Keep it going")
                print(awinner)
            else:
                print("You're wrong. You got {} right.".format(i))
                print(awinner)
        else:
            if A["follower_counter"] > B["follower_counter"]:
                print("You're wrong. You got {} right.".format(i))
                print(awinner)
            else:
                l += 1
                i += 1
                print("You're right. Keep it going")
                print(awinner)

highorlower()
