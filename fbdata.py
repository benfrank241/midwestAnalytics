# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl
# from sqlalchemy import create_engine
# # Import data manipulation modules
# import pandas as pd
# import pymysql
# import numpy as np
# # Import data visualization modules
# import matplotlib as mpl
# import matplotlib.pyplot as plt


#Data to collect

#Overall
#4th Down conversion rate (per team and yardage)
#field goal conversion rate (per team and yardage)
#Avg Punt net
#Extra Point success rate(maybe league wide)
#Yards per first down


#Per Drive
#Drive Success rate


#PAT conversion (per team)
patPC = {"GC" : 1.000, "CC" : 0.926, "RC" : 0.917, "BC" : 0.905, "MC" : 0.903, "LFC" : 0.898, "KC" : 0.880, "IC" : 0.857, "UoC" : 0.791, "LU" : 0.750, "MWC" : 0.882}

pNet = {"GC" : 27.7, "CC" : 29.7, "RC" : 28.4, "BC" : 24.1, "MC" : 29.3, "LFC" : 32.1, "KC" : 30.3, "IC" : 29.5, "UoC" : 31.0, "LU" : 28.3, "MWC" : 29.0}


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

fDowns = {"GC" : 96, "CC" : 139, "RC" : 176, "BC" : 83, "MC" : 159, "LFC" : 158, "KC" : 128, "IC" : 112, "UoC" : 192, "LU" : 60, "MWC" : 130}

nDrives = {"GC" : 86, "CC" : 74, "RC" : 114, "BC" : 88, "MC" : 105, "LFC" : 97, "KC" : 83, "IC" : 104, "UoC" : 103, "LU" : 91, "MWC" : 95}

nTD = {"GC" : 11, "CC" : 28, "RC" : 49, "BC" : 21, "MC" : 57, "LFC" : 44, "KC" : 24, "IC" : 33, "UoC" : 45, "LU" : 9, "MWC" : 32}

setsOfDowns = {}
#Sets of downs = Drives + First downs - TDs
for i in fDowns:
    setsOfDowns[i] = (nDrives[i] + fDowns[i] - nTD[i])

# print(setsOfDowns)

#Drive Success rate = first downs / setsofdowns
driveSuccess = {}
for i in setsOfDowns:
    driveSuccess[i] = fDowns[i] / setsOfDowns[i]


# print(driveSuccess)


#TODO: 4th down (what do I need to collect)
#Per 4th down attempt
#Score Difference?
#Time remaining?
#Yard line?
#Yards to go.
#Success.

#i could be lazy and just grab 4th down%

# import re
# import box
#
#
# def collect_fourth_down_data():
#     current_team = ""
#     teams_fourth_down_data = {}
#
#     with open('box.txt', 'r') as f:
#         fourth_down_pattern = re.compile(r'(4th and \d+)')
#         team_start_drive_pattern = re.compile(r'([A-Z][a-z]+ [A-Z][a-z]+).* drive start')
#         for line in f:
#             match = fourth_down_pattern.search(line)
#             team_drive_start = team_start_drive_pattern.search(line)
#             if match:
#                 distance = match.group(1)
#                 if current_team not in teams_fourth_down_data:
#                     teams_fourth_down_data[current_team] = {"attempted": 0, "converted": 0, "distances": []}
#                 teams_fourth_down_data[current_team]["attempted"] += 1
#                 teams_fourth_down_data[current_team]["distances"].append(distance)
#                 if "converted" in line:
#                     teams_fourth_down_data[current_team]["converted"] += 1
#                 elif team_drive_start:
#                     current_team = team_drive_start.group(1)
#     return teams_fourth_down_data


import re

teams = ["Cornell", "Beloit", "Illinois", "UChicago", "Monmouth (IL)", "Grinell"]
fourth_data = []


def collect_fourth_down_data():
    
    current_team = ""
    with open('box.txt', 'r') as f:
        # Use regular expressions to search for the relevant information in the box score
        fourth_down_pattern = re.compile(r'(4th and \d+)')
        for line in f:

            line = line.split(" ") #split 

            if len(line) <= 6 and "at" in line:
                if line[0] in teams:
                    current_team = line[0]
                    # print(current_team)
            line = " ".join(line)
            match = fourth_down_pattern.search(line)
            if match:
                result = "unknown"
                line = line.split(" ")
                down = " ".join(line[0:3])
                distance = line[4]
                if "PENALTY" in line:
                    continue
                if "punt" in line:
                    result = "Punt"
                if "field" in line:
                    if "NO" in line:
                        result = "Field Goal NO GOOD"
                    else:
                        result = "Field Goal GOOD"
                
                if "incomplete" in line:
                    result = "Failed"
                if "TOUCHDOWN," in line:
                    result = "TD"
                if "1ST" in line:
                    result = "SUCCESS"
                if "End" in line:
                    continue
                if "Start" in line:
                    continue
                if "Timeout" in line:
                    continue
                if "ball" in line:
                    result = "Failed"
                if "loss" in line:
                    result = "Failed"

                if result == "unknown":
                    print(" ".join(line))
                    raise Exception("UKNOWN RESULT")


                fourth_data.append([current_team + " " + down + " " + distance + " " + result])
                

        

collect_fourth_down_data()
# print(fourth_data)
for i in fourth_data:
    print(i)
