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

context = ssl._create_unverified_context()

url = 'https://static.midwestconference.org/custompages/Statistics/2021-22/bb/HTML/lgplyrs.htm#leagp.mlb'

html = urlopen(url, context=context)

stats_page = BeautifulSoup(html, 'html.parser')

data = stats_page.findAll('pre')[0]
# column_headers = [i.getText() for i in column_headers.findAll('th')]

data = str(data)
# Split the data into lines
lines = data.split("\n")
#Remove first garbage lines from dataset
lines = lines[8:]
lines = list(filter(None, lines))
# Extract the column names from the first line
o_column_names = lines[0].split()
# Initialize an empty list to store the parsed data
o_column_names.insert(1, 'Team')
# Extract the pitching stat columns
p_column_names = lines[257].split()
p_column_names.insert(1, 'Team')
# print(p_column_names)
# Extract the defensive stat columns
d_column_names = lines[453].split()
d_column_names.insert(1, 'Team')
# print(d_column_names)

o_stats = []
# all_stats = []
#collects o_stats
for i in range(2, len(lines)):
        if "AVG" in lines[i]:
            continue
        if len(lines[i]) > 15 and '<hr>' not in lines[i]:
            # print(lines[i])
            o_stats.append(lines[i].split())
        if "Ripple" in lines[i]:
            break
#cleans names in o_stats
for i in range(len(o_stats)):
    if o_stats[i]:
        if len(o_stats[i]) > 21:
            o_stats[i].remove(o_stats[i][0])
        o_stats[i][0] = o_stats[i][0].replace(',', '')
        if '.' in o_stats[i][0] and len(o_stats[i][0]) == 2:
            o_stats[i].remove(o_stats[i][0])
            o_stats[i][0] = o_stats[i][0].replace(',', '')
            # print(o_stats[i])
    if o_stats[i] and len(o_stats[i]) > 6:
        if '...' in o_stats[i][1]:
            # print(o_stats[i][1])
            o_stats[i][1] = o_stats[i][1].replace('.','')

#collects all pitching stats
p_stats = []
for i in range(257, len(lines)):
        if "HBP" in lines[i]:
            continue
        if "Z. Kennedy" in lines[i]:
            continue
        if "La Rosa" in lines[i]:
            lines[i] = lines[i].replace("De La Rosa", "DeLaRosa")
        if len(lines[i]) > 15 and '<hr>' not in lines[i]:
            # print(lines[i])
            p_stats.append(lines[i].split())
        if "Lavoie" in lines[i]:
            break

#cleans names in pitching stats
for i in range(len(p_stats)):
    if p_stats[i]:
        if len(p_stats[i]) > 23:
            p_stats[i].remove(p_stats[i][0])
            # print(p_stats[i])
        p_stats[i][0] = p_stats[i][0].replace(',', '')
        if '.' in p_stats[i][0] and len(p_stats[i][0]) == 2:
            p_stats[i].remove(p_stats[i][0])
            p_stats[i][0] = p_stats[i][0].replace(',', '')
            # print(o_stats[i])
    if p_stats[i] and len(p_stats[i]) > 6:
        if '...' in p_stats[i][1]:
            # print(o_stats[i][1])
            p_stats[i][1] = p_stats[i][1].replace('.','')


d_stats = []
for i in range(543, len(lines)):
        if "CSB" in lines[i]:
            continue
        if "Z. Kennedy" in lines[i]:
            continue
        if "La Rosa" in lines[i]:
            lines[i] = lines[i].replace("De La Rosa", "DeLaRosa")
        if len(lines[i]) > 15 and '<hr>' not in lines[i]:
            # print(lines[i])
            d_stats.append(lines[i].split())
        if "Shoenke" in lines[i]:
            break

#cleans defensive stats
for i in range(len(d_stats)):
    if d_stats[i]:
        if len(d_stats[i]) > 13:
            d_stats[i].remove(d_stats[i][0])
            # print(p_stats[i])
        d_stats[i][0] = d_stats[i][0].replace(',', '')
        if '.' in d_stats[i][0] and len(d_stats[i][0]) == 2:
            d_stats[i].remove(d_stats[i][0])
            d_stats[i][0] = d_stats[i][0].replace(',', '')
            # print(o_stats[i])
    if d_stats[i] and len(d_stats[i]) > 6:
        if '...' in d_stats[i][1]:
            # print(o_stats[i][1])
            d_stats[i][1] = d_stats[i][1].replace('.','')

#Create DataFrame from our scraped data
tableName = "defense"
# print(o_column_names)
data = pd.DataFrame(o_stats, columns=o_column_names)

cata = ['AVG', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'TB', 'SLG%', 'BB', 'HBP', 'SO', 'GDP', 'OB%', 'SF', 'SH']

#change data types so we can make calculations
for i in cata:
    data[i] = pd.to_numeric(data[i])

data["SO%"] = (data["SO"]) / (data["AB"])
# print(data.head())

# print(data.dtypes)







#upload to MySQL
# sqlEngine = create_engine('mysql+pymysql://root:root2023@localhost:3306/baseball')
#
# dbConnection = sqlEngine.connect()
#
# try:
#
#     frame = DataFrame.to_sql(tableName, dbConnection, if_exists='fail');
#
# except ValueError as vx:
#
#     print(vx)
#
# except Exception as ex:
#
#     print(ex)
#
# else:
#
#     print("Table %s created successfully." % tableName);
#
# finally:
#
#     dbConnection.close()

