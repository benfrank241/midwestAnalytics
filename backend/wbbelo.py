from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
from sqlalchemy import create_engine
import pandas as pd
import math


context = ssl._create_unverified_context()

url = 'https://static.midwestconference.org/custompages/Statistics/2021-22/wbb/HTML/CONFSTAT.HTM'

html = urlopen(url, context=context)

soup = BeautifulSoup(html, 'html.parser')

data = soup.get_text()

data = str(data)

data = data.split("\n")

data = data[33:]

# print(data[0:10])

for i, line in enumerate(data):
    data[i] = data[i].replace(u'\xa0', u' ')
    data[i] = data[i].replace("Box score ", '')
    data[i] = data[i].replace("  ", '')
    # data[i] = data[i].replace(",", '')

while("" in data):
    data.remove("")

# print(data[0:100])

def calculate(winner, wScore, loser, lScore):
    print("Winner:", winner)
    print("Loser:", loser)
    print("Score diff", int(wScore) - int(lScore))

games = []

for i in range(2,383,3):
    games.append(data[i])

# print(games)

for i, line in enumerate(games):
    line = line.split(",")

    wName = line[0].rstrip('0123456789')
    wScore = line[0][len(wName):]
    lName = line[1].rstrip('0123456789')
    lScore = line[1][len(lName):]
    calculate(wName,wScore,lName,lScore)
    # print(wName)
    # print(wScore)
    # print(lName)
    # print(lScore)

    



