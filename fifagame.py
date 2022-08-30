import json
import random

with open('players.json', 'r', encoding="utf-8") as b:
    playerdata = json.load(b)

def higherorlower():
    A = random.choice(playerdata)
    B = random.choice(playerdata)
    question = "Who has the better overall: A {} or B {}".format(A["short_name"], B["short_name"])
    print(question)
    userchoice = input("Choose A or B: ").upper()

higherorlower()
