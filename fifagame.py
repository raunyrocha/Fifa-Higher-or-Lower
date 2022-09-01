import json
import random

with open('players.json', 'r', encoding="utf-8") as data:
    playerdata = json.load(data)

winnerex = ["Bingo", "Good one", "On the spot", "You're right"]
loserex = ["Wroooong", "You suck at this", "Nice try", "Own goal"]

winnermsg = random.choice(winnerex)
losermsg = random.choice(loserex)

list_continue = []

def initiallist():
    A = random.choice(playerdata)
    B = random.choice(playerdata)
    list_continue.append(A)
    list_continue.append(B)


initiallist()
print(list_continue)
