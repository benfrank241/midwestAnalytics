#this file is able to read from the MySQL database
from sqlalchemy import create_engine
import pymysql
import pandas as pd
import math


sqlEngine = create_engine('mysql+pymysql://root:root2023@localhost:3306/testdatabase')

dbConnection = sqlEngine.connect()

frame = pd.read_sql("select * from baseball.pitching", dbConnection);

pd.set_option('display.expand_frame_repr', False)

# print(frame)

dbConnection.close()

#WAR = [[([(League “FIP” – “FIP”) / Pitcher Specific Runs Per Win] + Replacement Level) * (IP/9)] * Leverage Multiplier for Relievers] + League Correction
#https://library.fangraphs.com/war/calculating-war-pitchers/

#basic https://www.fangraphs.com/leaders.aspx?pos=all&stats=pit&lg=all&qual=y&type=8&season=2022&month=0&season1=2022&ind=0