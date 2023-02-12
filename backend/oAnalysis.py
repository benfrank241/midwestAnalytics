#this file is able to read from the MySQL database
from sqlalchemy import create_engine, text
from sqlalchemy import *
import pymysql
import pandas as pd
import numpy as np
import math
import os

p = os.environ.get('CLOUD_SQL_PASSWORD')

i = 'mysql+pymysql://ben:'+p+'@34.29.90.189/baseball'

sqlEngine = create_engine(i)

dbConnection = sqlEngine.connect()

query = text("SELECT * from baseball.offense")

frame = pd.read_sql(query, dbConnection);

# pd.set_option('display.expand_frame_repr', False)

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
frame["ISO"] = round((frame["SLG%"]) - (frame["AVG"]),3)
#BABIP
frame["BABIP"] = round((frame["H"] - frame["HR"]) / (frame["AB"] - frame["HR"] - frame["SO"] + frame["SF"]), 3)
#RC round this one to the ones digit
frame["RC"] = round((frame["TB"] * (frame["H"] + frame["BB"]) / (frame["AB"] + frame["BB"])), 0)

#wOBA https://library.fangraphs.com/offense/woba/
frame["wOBA"] = round(((frame["BB"] * 0.69) + (frame["HBP"] * 0.722) + (frame["1B"] * 0.888) + (frame["2B"] * 1.271) + (frame["3B"] * 1.616) + (frame["HR"] * 2.101)) / (frame["AB"] + frame["BB"] + frame["SF"] + frame["HBP"]), 3)

opsAvg = frame["OPS"].mean()
slgAvg = frame["SLG%"].mean()
avgAvg = frame["AVG"].mean()
wOBAAvg = frame["wOBA"].median()
#ops+
frame["OPS+"] = round((100 * (frame["OPS"] / opsAvg) + (frame["SLG%"] / slgAvg) - 1), 0)
#avg+
frame["AVG+"] = round((100 * (frame["AVG"] / avgAvg) -1), 0)

# del frame["index"]


#WAR = (Batting Runs + Base Running Runs + Fielding Runs + Positional Adjustment + League Adjustment +Replacement Runs) / (Runs Per Win)
#https://library.fangraphs.com/war/war-position-players/

frame["Rating"] = round(((frame["wOBA"] - wOBAAvg)/1.2 + (frame["OPS"] - opsAvg)/1.2),3)
frame=frame.drop(frame.index[0])
# frame.drop([0])
# print(frame.head())
frame.replace([np.inf, -np.inf], np.nan, inplace=True)
frame.dropna(inplace=True)
frame.rename(columns={'GP-GS': 'GP_GS', 'SB-ATT': 'SB_ATT'}, inplace=True)



cata = ['Player', 'Team', 'GP_GS', 'AVG', 'AB', 'R', 'H','1B', '2B', '3B', 'HR', 'RBI', 'TB', 'SLG%', 'BB', 'HBP', 'SO', 'GDP', 'OB%', 'SF', 'SH', 'SB_ATT', 'SO%', 'BB%', 'BB/K', 'ISO', 'BABIP', 'RC', 'wOBA', 'OPS', 'OPS+', 'AVG+', 'Rating']

#change data types so we can make calculations
for i in cata:
    frame[i] = frame[i].astype(object)

data = pd.DataFrame(frame)

# print(data.head())
# print(data.dtypes)
frame["Player"] = frame["Player"].replace("S.Richardson", "Richardson")

print(data.to_csv(index=False))


sqlEngine = create_engine('mysql+pymysql://ben:'+p+'@34.29.90.189/analysis')
dbConnection = sqlEngine.connect()

try:

    frame = data.to_sql("ten", dbConnection, if_exists='fail')

except ValueError as vx:

    print(vx)

except Exception as ex:

    print(ex)

else:

    print("Table 'ten' created successfully.")

finally:

    dbConnection.close()


# todo: upload these stats to google mysql, get backend to call the right stats
