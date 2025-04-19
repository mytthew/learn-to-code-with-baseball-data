#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 10:02:19 2025

@author: matt
"""

# 3.0.1 - Load the 2018 aggregated pithcing data into a DataFrame named dfp. You'll use it for the rest  of the problems in this section. 
import pandas as pd
from os import path
import os

DATA_DIR = '/Users/matt/Desktop/learn-to-code-with-baseball-data/data'

dfp = pd.read_csv(
    path.join(DATA_DIR, '2018-season', 'pitches.csv'))

print(dfp.head())

# 3.0.2 - Use the dfp DataFrame to create another DataFrame, dfp50, that is the top 50 (by lowest ERA) players. 
# BONUS: I'm only going to return the player, their team, and their ERA. Then,  reset the index to the player's last name. 
lowest50ERA = dfp.sort_values('ERA')[['nameFirst', 'nameLast', 'teamID', 'ERA']]
lowest50ERA.set_index('nameLast', inplace=True)
print(lowest50ERA.head(50))

# 3.0.3 - Sort dfp by first name in descending order (so Zack Greink is first)
# BONUS: Only return the player's first and last name and team. Then, reset the index to the player's first name. 
alph_order1 = dfp.sort_values('nameFirst', ascending=False)[['nameFirst', 'nameLast', 'teamID']]
alph_order1.set_index('nameFirst', inplace=True)
print(alph_order1.head(10))

# 3.0.4 = What is the type of dfp.sort_values('W')?
sorted_dfp = dfp.sort_values('W')
print(type(sorted_dfp))

# answer: <class 'pandas.core.frame.DataFrame'>

# 3.0.5a - Make a new DataGFrame, dfp_simple, with just the columns 'nameFirst', 'nameLast', 'W', 'L', and 'ERA' in that order. 
dfp_simple = dfp[['nameFirst', 'nameLast', 'W', 'L','ERA']]
print(dfp_simple.head())

# 3.0.5b - Rearrange dfp_simple so the order is 'nameLast', 'nameFirst', 'ERA','W', 'L'
dfp_simple = dfp_simple[['nameLast', 'nameFirst', 'ERA', 'W', 'L']]
print(dfp_simple.head())

# 3.0.5c - Using the original dfp  DataFrame, add the 'teamID' column to dfp_simple
dfp_simple['teamID'] = dfp['teamID']
print(dfp_simple.head())

# Prepare the folder for output
folder_path = '/Users/matt/Desktop/learn-to-code-with-baseball-data/pandas'
os.makedirs(folder_path, exist_ok=True)  # ✅ only creates the folder

#  3.0.5d - Write a copy of dfp_simple to ./data/problems/dfp_simple.txt. Make it '|' (pipe) delimited instead of ',' (comma)  delimited. 
file_path = os.path.join(folder_path, 'dfp_simple.txt')
dfp_simple.to_csv(file_path, sep='|', index=False)



 


























