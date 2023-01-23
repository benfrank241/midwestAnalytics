from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
from sqlalchemy import create_engine
# Import data manipulation modules
import pandas as pd
import pymysql
import numpy as np
# Import data visualization modules
import matplotlib as mpl
import matplotlib.pyplot as plt


#Data to collect

#Overall
#4th Down conversion rate (per team and yardage)
#field goal conversion rate (per team and yardage)
#Avg Punt net
#Extra Point success rate(maybe league wide)
#Yards per first down


#Per Drive
#Drive Success rate

#Per 4th down attempt
#Score Differnce
#Time remaining
#Yard line
#Yards to go


#PAT conversion (per team)
patPC = {"GC" : 1.000, "CC" : 0.926, "RC" : 0.917, "BC" : 0.905, "MC" : 0.903, "LFC" : 0.898, "KC" : 0.880, "IC" : 0.857, "UoC" : 0.791, "LU" : 0.750, "MWC" : 0.882}

pNet = {"GC" : 27.7, "CC" : 29.7, "RC" : 28.4, "BC" : 24.1, "MC" : 29.3, "LFC" : 32.1, "KC" : 30.3, "IC" : 29.5, "UoC" : 31.0, "LU" : 28.3, "MWC" : 29.0}


#pseduocode to find drive success rate
#collecting number of 
#read play by play section line-by-line
#if it doesnt start with a number > continue
#find out who has the ball
#1st first down is marked
#Find "1ST DOWN" or "TOUCHDOWN" or "NO GOOD"
#

#Drive success rate =https://www.footballperspective.com/how-to-calculate-drive-success-rate/#:~:text=So%20to%20calculate%20the%20number%20of%20drives%2C%20you%20can%20either,%2Ffield%20goal%20attempts%2Ftouchdowns.
#First downs / Number of drives that dont end the game
#Sets of downs = Drives + First downs - TDs


#NUMBER OF FIRST DOWNS : NUMBER OF DRIVES
#Knox
#6:13 25:8 20:10 10:13 15:8 24:8 14:9 19:9 5:12 TOTAL: 128:83
#MON
#19:13 19:16 20:12 28:13 13:12 18:12 26:14 16:13 TOTAL: 159:105
#LU
#3:16 3:13 12:9 12:11 17:7 13:12 10:12 2:11 TOTAL: 60:91
#RIP
#22:12 14:17 28:12 16:11 13:14 17:11 23:13 25:11 18:13 TOTAL: 176:114
#LFC
#15:8 16:12 18:10 20:9 11:15 15:13 23:10 19:9 21:11 TOTAL: 158:97
#UC
#16:8 19:11 22:13 18:12 26:10 22:12 26:10 27:11 16:16 TOT: 192:103
#BELOIT
#7:15 0:11 10:11 6:13 17:8 16:11 11:11 16:8 TOT: 83:88
#IC
#21:16 15:12 15:13 23:10 8:14 11:12 8:14 11:17 TOT: 112:104
#GRI
#14:8 8:12 2:9 18:8 11:13 22:11 15:12 6:13 TOT: 96:86
#COR
#19:8 16:9 19:13 12:9 20:6 15:11 15:11 23:7 TOT: 139:74
