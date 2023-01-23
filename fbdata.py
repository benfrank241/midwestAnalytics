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

#Drive success rate = 
#First downs / Number of drives 

