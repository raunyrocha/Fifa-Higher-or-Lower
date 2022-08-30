import json
import random

with open('players.json', 'r', encoding="utf-8") as b:
    playerdata = json.load(b)
    for player in playerdata:
        print("{} is a {} who plays for {} . He has a overall of {}.".format(player["short_name"], player["player_positions"], player["club_name"], player["overall"]))

def higherorlower():
    A = random.choice(gamerdata)
    B = random.choice(gamerdata)
    question = "Who has the better overall: A {} or B {}".format(A["short_name"], B["short_name"])
    print(question)
    userchoice = input("Choose A or B: ").upper()

higherorlower()
