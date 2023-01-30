#this file is able to read from the MySQL database
from sqlalchemy import create_engine
import pymysql
import pandas as pd
import math


sqlEngine = create_engine('mysql+pymysql://root:root2023@localhost:3306/baseball')

dbConnection = sqlEngine.connect()

frame = pd.read_sql("select * from baseball.offense", dbConnection);

pd.set_option('display.expand_frame_repr', False)

# print(frame)

dbConnection.close()

cata = ['AVG', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'TB', 'SLG%', 'BB', 'HBP', 'SO', 'GDP', 'OB%', 'SF', 'SH']

#change data types so we can make calculations
for i in cata:
    frame[i] = pd.to_numeric(frame[i])

#Create SO%
frame["SO%"] = round((frame["SO"]) / (frame["AB"]), 3)
#BB%
frame["BB%"] = round((frame["BB"]) / (frame["AB"]), 3)
#BB/K
frame["BB/K"] = round((frame["BB"]) / (frame["SO"]), 3)
#Single, inserting it in the proper place in the df
frame["temp"] = (frame["H"] - frame["2B"] - frame["3B"] - frame["HR"])
frame.insert(8, "1B", frame["temp"])
del frame["temp"]
#OPS
frame["OPS"] = round(frame["OB%"] + frame["SLG%"], 3)
#ISO
frame["ISO"] = (frame["SLG%"]) - (frame["AVG"])
#BABIP
frame["BABIP"] = round((frame["H"] - frame["HR"]) / (frame["AB"] - frame["HR"] - frame["SO"] + frame["SF"]), 3)
#RC round this one to the ones digit
frame["RC"] = round((frame["TB"] * (frame["H"] + frame["BB"]) / (frame["AB"] + frame["BB"])), 0)

#wOBA https://library.fangraphs.com/offense/woba/
frame["wOBA"] = round(((frame["BB"] * 0.69) + (frame["HBP"] * 0.722) + (frame["1B"] * 0.888) + (frame["2B"] * 1.271) + (frame["3B"] * 1.616) + (frame["HR"] * 2.101)) / (frame["AB"] + frame["BB"] + frame["SF"] + frame["HBP"]), 3)

opsAvg = frame["OPS"].mean()
slgAvg = frame["SLG%"].mean()
avgAvg = frame["AVG"].mean()
#ops+
frame["OPS+"] = round((100 * (frame["OPS"] / opsAvg) + (frame["SLG%"] / slgAvg) - 1), 0)
#avg+
frame["AVG+"] = round((100 * (frame["AVG"] / avgAvg) -1), 0)

del frame["index"]
# print(frame.head())

#WAR = (Batting Runs + Base Running Runs + Fielding Runs + Positional Adjustment + League Adjustment +Replacement Runs) / (Runs Per Win)
#https://library.fangraphs.com/war/war-position-players/

