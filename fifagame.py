import json
import random

with open('players.json', 'r', encoding="utf-8") as data:
    playerdata = json.load(data)

winnerex = ["Bingo!", "Good one", "On the spot", "You're right"]
loserex = ["Wroooong", "You suck at this", "Nice try", "Own goal"]

winnermsg = random.choice(winnerex)
losermsg = random.choice(loserex)

list_continue = []

def initiallist():
#this function initializes the game with two random players and append them to the list that runs the data for the questions.
    A = random.choice(playerdata)
    B = random.choice(playerdata)
    list_continue.append(A)
    list_continue.append(B)

def game():
#this runs the game, updates the game list and the counter for attempts.
    game.counter += 1
    A = list_continue[0]
    B = list_continue[1]
    ahigher = "{} has the higher overall with {}".format(A["short_name"], A["overall"])
    bhigher = "{} has the higher overall with {}".format(B["short_name"], B["overall"])
    tied = "It's a tie. Try another one."
    question = "Who has the highest overall on fifa 22?\nA - {}, {} from {}\nB - {}, {} from {}".format(A["short_name"], A["player_positions"], A["club_name"], B["short_name"], B["player_positions"], B["club_name"])
    print(question)
    userchoice = input("What's your choice? Type (A) or (B):\n ").upper()
    if A["overall"] > B["overall"]:
        if userchoice == "A":
            print(winnermsg)
            print(ahigher)
            list_continue.pop(0)
            list_continue.append(random.choice(playerdata))
            game()
        elif userchoice == "B":
            print(losermsg)
            print(ahigher)
        else:
            print("Invalid choice. Try again.")
            inputerror()

    elif B["overall"] > A["overall"]:
        if userchoice == "B":
            print(winnermsg)
            print(bhigher)
            list_continue.pop(0)
            list_continue.append(random.choice(playerdata))
            game()
        elif userchoice == "A":
            print(losermsg)
            print(bhigher)
        else:
            print("Invalid choice. Try again.")
            inputerror()

    else:
        print(tied)
        tiedgame()


game.counter = 0

def tiedgame():
#this function is called when the overall is tied.
    tiedgame.counter += 1
    game()

tiedgame.counter = 0

def inputerror():
    inputerror.counter += 1
    game()

inputerror.counter = 0


initiallist()
game()
