#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 09:15:08 2025

@author: matt
"""

# 3.1.1 - Load the at bat data from ./data/100-game-sample/atbats.csv into a Data Frame named dfb. You'll use it for the rest of the problems in this section. 
import pandas as pd
from os import path
import os

DATA_DIR = '/Users/matt/Desktop/learn-to-code-with-baseball-data/data'

dfb = pd.read_csv(
    path.join(DATA_DIR, '100-game-sample', 'atbats (1).csv'))

print(dfb.head())

# 3.1.2 - Add a column to dfb, 'runs_scored' that gives runs scored this at bat (hint: use 'b_score_start' and 'b_score_end' columns). 
dfb['runs_scored'] = dfb['b_score_end'] - dfb['b_score_start']
#Check to see that the column was added 
print(dfb.columns)
#Now let's  get a view of the first five rows of the dataframe 
print(dfb.head())

# 3.1.3 - Add a column 'ab_desc' to dfb that takes the form, 'got  a vs',  e.g. 'A. Eaton got a single vs S.Romano' for line one. 
dfb['ab_desc'] = dfb['batter'] + ' got a ' + dfb['event'] + ' vs ' + dfb['pitcher']

# Check to ensure it's working
print(dfb['ab_desc'].head())

# 3.1.4 - Add a boolean column to dfb called 'final_out' that indicates whether the at bat was the final out of the inning.
dfb['final_out'] = dfb['o'] == 3
print(dfb['final_out'].head())

# 3.1.5 - Add a column 'len_last_name' that gives the length of the pitcher's last name.
dfb['len_last_name'] = dfb['pitcher'].str.split('.').str[1].str.len()
print(dfb[['pitcher', 'len_last_name']].head())

# 3.1.6 - 'ab_id' is a numeric column, but its not really meant for doing math, change it into a string column.
dfb['ab_id'] = dfb['ab_id'].astype(str)
print("ab_id type:", dfb['ab_id'].dtype)

# 3.1.7a - Let's make the columns in dfb more readable. Replace all the '_' with ' ' in all the columns. 
dfb.columns = dfb.columns.str.replace('_', ' ')
print(dfb.columns)

# 3.1.7b - This actually isn't good practice. Change it back. 
dfb.columns = dfb.columns.str.replace(' ', '_')
print(dfb.columns)

# 3.1.8a - Using the 'runs_scored' columns you created above, make a new column 'run_portion' indicating the % of the batting team's total runs scored during this at bat.  
dfb['run_portion'] = dfb['runs_scored'] / dfb['b_score_end']
print(dfb[['batter', 'runs_scored', 'b_score_end', 'run_portion']].head())

# 3.1.8b - There are missing values in this column, why? Replace all the missing values with -99. 
# Answer: If the runs scored are 0 and the runs scored at the end of the at bat are also 0, then we'll get a NaN value. 
dfb['run_portion'] = dfb['run_portion'].fillna(-99)

# 3.1.9 - Drop the column 'run_portion'. In another line, confirm that it worked. 
dfb.drop(columns='run_portion', inplace=True)
print(dfb.columns) 




