#this file is able to read from the MySQL database


from sqlalchemy import create_engine
import pymysql
import pandas as pd


sqlEngine = create_engine('mysql+pymysql://root:root2023@localhost:3306/testdatabase')

dbConnection = sqlEngine.connect()

frame = pd.read_sql("select * from baseball.offense", dbConnection);

pd.set_option('display.expand_frame_repr', False)

print(frame)

dbConnection.close()

cata = ['AVG', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'TB', 'SLG%', 'BB', 'HBP', 'SO', 'GDP', 'OB%', 'SF', 'SH']

#change data types so we can make calculations
for i in cata:
    frame[i] = pd.to_numeric(frame[i])

#Create SO%
frame["SO%"] = (frame["SO"]) / (frame["AB"])
#Single
frame["1B"] = (frame["H"] - frame["2B"] - frame["3B"] - frame["HR"])
#OPS
frame["OPS"] = (frame["H"] + frame["BB"] + frame["HBP"]) / (frame["AB"] + frame["BB"] + frame["HBP"] + frame["SF"])
#ISO
frame["ISO"] = (frame["SLG%"]) - (frame["AVG"])
#BABIP
frame["BABIP"] = (frame["H"] - frame["HR"]) / (frame["AB"] - frame["HR"] - frame["SO"] + frame["SF"])
#RC round this one to the ones digit
frame["RC"] = (frame["TB"] * (frame["H"] + frame["BB"]) / (frame["AB"] + frame["BB"]))
#wOBA https://library.fangraphs.com/offense/woba/
frame["wOBA"] = ((frame["BB"] * 0.69) + (frame["HBP"] * 0.722) + (frame["1B"] * 0.888) + (frame["2B"] * 1.271) + (frame["3B"] * 1.616) + (frame["HR"] * 2.101)) / (frame["AB"] + frame["BB"] + frame["SF"] + frame["HBP"])


#TODO: insert 1B into the proper place, round and + stats
#need to collect conference avg for avg+ slg+ etc
print(frame.head())

