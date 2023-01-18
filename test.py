#this file is able to read from the MySQL database


from sqlalchemy import create_engine
import pymysql
import pandas as pd

sqlEngine = create_engine('mysql+pymysql://root:root2023@localhost:3306/testdatabase')

dbConnection = sqlEngine.connect()

frame = pd.read_sql("select * from testdatabase.baseballoffensivestats", dbConnection);

pd.set_option('display.expand_frame_repr', False)

print(frame)

dbConnection.close()