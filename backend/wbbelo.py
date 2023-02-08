from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
from sqlalchemy import create_engine
import pandas as pd
import math

teams = {"Beloit": 1000, "Cornell": 1000, "Grinnell": 1000, "Lawrence": 1000, "Monmouth": 1000, "IllinoisCollege": 1000, "Knox":1000, "Ripon":1000}

#ELO Model
def calculate(winner, wScore, loser, lScore):
    print("Winner:", winner)
    print("Loser:", loser)
    print("Score diff", int(wScore) - int(lScore))

def Probability(rating1, rating2):
    return 1.0 * 1.0 / (1 + 1.0 * (math.pow(10, 1.0 * (rating1 - rating2) / 400)))

def EloRating(Ra, Rb, K, d):
    # To calculate the Winning
    # Probability of Player B
    if Ra not in teams or Rb not in teams:
        # print("Team not found")
        return

    Pb = Probability(teams[Ra], teams[Rb])

    # To calculate the Winning
    # Probability of Player A
    Pa = Probability(teams[Rb], teams[Ra])


    # Updating the Elo Ratings
    teams[Ra] = teams[Ra] + K * (1 - Pa)
    teams[Rb] = teams[Rb] + K * (0 - Pb)

    # print("Updated Ratings:-")
    # print(Ra, " =", round(teams[Ra], 6), Rb, " =", round(teams[Rb], 6))
    return

#for current season
teams2 = {"BeloitCollege": 1000, "CornellCollege": 1000, "GrinnellCollege": 1000, "LawrenceUniversity": 1000, "MonmouthCollege": 1000, "IllinoisCollege": 1000, "KnoxCollege": 1000, "RiponCollege":1000, "LakeForestCollege":1000}


def EloRating2(Ra, Rb, K, d):
    # To calculate the Winning
    # Probability of Player B
    if Ra not in teams2 or Rb not in teams2:
        # print("Team not found")
        return

    Pb = Probability(teams2[Ra], teams2[Rb])

    # To calculate the Winning
    # Probability of Player A
    Pa = Probability(teams2[Rb], teams2[Ra])


    # Updating the Elo Ratings
    teams2[Ra] = teams2[Ra] + K * (1 - Pa)
    teams2[Rb] = teams2[Rb] + K * (0 - Pb)

    # print("Updated Ratings:-")
    # print(Ra, " =", round(teams2[Ra], 6), Rb, " =", round(teams2[Rb], 6))
    return







#Data Scraping and cleaning
context = ssl._create_unverified_context()

url = 'https://static.midwestconference.org/custompages/Statistics/2021-22/wbb/HTML/CONFSTAT.HTM'

html = urlopen(url, context=context)

soup = BeautifulSoup(html, 'html.parser')

data = soup.get_text()

data = str(data)

data = data.split("\n")

data = data[33:]


for i in range(len(data)):
    data[i] = data[i].replace(u'\xa0', u' ')
    data[i] = data[i].replace("Box score ", '')
    data[i] = data[i].replace("  ", '')
    # data[i] = data[i].replace(",", '')

while("" in data):
    data.remove("")

# print(data[0:100])
games = []

for i in range(2,383,3):
    games.append(data[i])

# print(games[0:3])

for line in games:
    line = line.split(",")

    wName = line[0].rstrip('0123456789')
    wName = wName.replace(" ", "")
    wScore = line[0][len(wName):]
    lName = line[1].rstrip('0123456789')
    lName = lName.replace(" ", "")
    lScore = line[1][len(lName):]
    # diff = int(wScore) - int(lScore)
    EloRating(wName,lName,50,10)
    
    # print(wName)
    # print(lName)

    

    #todo: set up the elo system https://www.geeksforgeeks.org/elo-rating-algorithm/

currRes = []

with open('wbb.txt', 'r') as f:
    temp = ""
    for i, line in enumerate(f):
        # print(line)
        if i % 8 == 0: #Final Box Score
            continue
        if i % 8 == 1: #Millikin University
            continue
        if i % 8 == 2: #Millikin University
            temp += line
        if i % 8 == 3: #91
            temp += line + ","
        if i % 8 == 4: #Beloit College
            temp += line
        if i % 8 == 5: #Beloit College
            continue
        if i % 8 == 6: #51
            temp += line
            currRes.append(temp)
            temp = ""
        if i % 8 == 7: #Final
            continue

for i in range(len(currRes)):
    currRes[i] = currRes[i].replace(u'\n', u' ')
    currRes[i] = currRes[i].replace(u'\t', u' ')  
            
# print(currRes)

for line in currRes:
    # print(line)
    line = line.split(",")
    # print(line[0])

    wName = ''.join([i for i in line[0] if not i.isdigit()])
    wScore = line[0][len(wName)-1:]
    wName = wName.replace(" ", "")
    lName = ''.join([i for i in line[1] if not i.isdigit()])
    lScore = line[1][len(lName)-1:]
    lName = lName.replace(" ", "")

    if wScore < lScore:
        temp = wName
        wName = lName
        lName = temp
        temp = wScore
        wScore = lScore
        lScore = temp
    # print(wName)
    # print(wScore)
    # print(lName)
    # print(lScore)
    EloRating2(wName,lName,50,10)
    # diff = int(wScore) - int(lScore)

print("2021-22 Woman's basketball end of season ELO: ", teams)    
print("2022-23 Woman's basketball current ELO: ", teams2)
    

    



