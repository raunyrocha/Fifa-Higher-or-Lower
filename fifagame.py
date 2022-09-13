import json
import random
from datetime import date
from fgentries import avgtries, Alltries, totalplays

with open('players.json', 'r', encoding="utf-8") as data:
    playerdata = json.load(data)

winnerex = ["Bingo!", "Good one", "On the spot", "You're right"]
loserex = ["Wroooong", "You suck at this", "Nice try", "Own goal"]

winnermsg = random.choice(winnerex)
losermsg = random.choice(loserex)

username = input("Type your name for our scoreboard:\n")
date = date.today().strftime("%B %d, %Y")

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
    userchoice = input("What's your choice? Type (A) or (B):\n").upper()
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
            endgame()
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
            endgame()
        else:
            print("Invalid choice. Try again.")
            inputerror()

    else:
        print(tied)
        list_continue.pop(0)
        list_continue.append(random.choice(playerdata))
        tiedgame()


game.counter = 0

def tiedgame():
#this function is called when the overall is tied. Tied games do not count against the overall tries.
    tiedgame.counter += 1
    game()

tiedgame.counter = 0

def inputerror():
#this function is called when there is a input error. Input error do not count against the overall tries.
    inputerror.counter += 1
    game()

inputerror.counter = 0

tries = 0

def endgame():
#this prints the end of the game with the number of tries against the average of all players.
    tries = int(game.counter) - 1 - int(inputerror.counter) - int(tiedgame.counter)

    attempts = (int(Alltries) + int(tries)) / (int(totalplays) + 1)

    with open("tries.txt", "a+") as ac:
        # Move read cursor to the start of file.
        ac.seek(0)
        # If file is not empty then append '\n'
        data = ac.read(100)
        if len(data) > 0 :
            ac.write("\n")
        # Append text at the end of file
        ac.write(str(tries))

    print("Game over. {}, you've got {} right.".format(username, tries))
    print("The average attemps of all users is: {}.".format(round(attempts, 2)))

    with open("scoreboard.json", "r") as sb:
        bdict = json.load(sb)
        bdict.append({
            "Name": username,
            "Score": tries,
            "Date": date
        })

    with open("scoreboard.json", 'w') as json_file:
        json.dump(bdict, json_file,
                        indent=4,
                        separators=(',',': '))

    bdict.sort(key=lambda x: x.get('Score'), reverse=True)
    n = 0
    for item in bdict:
        if n < 11:
            n += 1
            print("{} - User: {}, Score {}, Date: {}".format(n, item["Name"], item["Score"], item["Date"]))

def main():
    initiallist()
    game()

if __name__ == '__main__':
    main()
