from statistics import mean
import json

totalplays = 0
totalpl = 0

with open("scoreboard.json", "r") as tries1:
    dict = json.load(tries1)
    newtries = []
    for item in dict:
        totalpl +=1
        newtries.append(int(item["Score"]))
    print(newtries)


with open("tries.txt", "r") as tries:
    listtries = tries.readlines()
    newlist = []
    for x in listtries:
        totalplays += 1
        newlist.append(int(x.replace("\n", "")))

def Average(l):
    avg = mean(l)
    return avg

Alltries = sum(newtries)

averagetries = Average(newtries)
avgtries = round(averagetries, 2)
