import json
import random

with open('players.json', 'r', encoding="utf-8") as b:
    playerdata = json.load(b)

winnerexpressions = ["Bingo", "Good one", "On the spot", "You're right"]
loserexpressions = ["Wroooong", "You suck at this", "Nice try", "Own goal"]

def higherorlower():
    A = random.choice(playerdata)
    B = random.choice(playerdata)
    ahigher = "{} has the higher overall with {}.".format(A["short_name"], A["overall"])
    bhigher = "{} has the higher overall with {}.".format(B["short_name"], B["overall"])
    question = "Who has the higher overall on FIFA 22: A - {}({} from {}) or B - {}({} from {})".format(A["short_name"], A["player_positions"], A["club_name"], B["short_name"], B["player_positions"], B["club_name"])
    print(question)
    userchoice = input("Choose A or B: ").upper()
    while userchoice == "A":
        if A["overall"] > B["overall"]:
            print(random.choice(winnerexpressions))
            print(ahigher)
            break
        else:
            print(random.choice(loserexpressions))
            print(bhigher)
            break

    while userchoice == "B":
        if A["overall"] > B["overall"]:
            print(random.choice(loserexpressions))
            print(ahigher)
            break
        else:
            print(random.choice(winnerexpressions))
            print(bhigher)
            break


higherorlower()
