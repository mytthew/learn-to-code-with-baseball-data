#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 09:11:17 2025

@author: matt
"""

# 3.2.1 - Load the batting data from ./data/2019-season/atbats.csv into a Dataframe named dfb. You'll use it for the rest of the problems in this section. 
import pandas as pd
from os import path
import os

DATA_DIR = '/Users/matt/Desktop/learn-to-code-with-baseball-data/data'

dfb = pd.read_csv(
    path.join(DATA_DIR, '2018-season', 'atbats.csv'))

print(dfb.head())

# 3.2.2 - Add a column to dfb that gives the total number of extra base hits for each player. 
# Do it two ways, one with basic arithmetic operators and another way using a built-in pandas function. 
# Call them 'extra_base1' and 'extra_base2'. Prove that they're the same. 
# First Way: 
print('--------------')
dfb['extra_base1'] = dfb['2B'] + dfb['3B'] +dfb['HR']
print(dfb[['name','extra_base1']].head())

#Second Way:
print('--------------')
dfb['extra_base2'] = dfb[['2B','3B','HR']].sum(axis=1)
print(dfb[['name','extra_base2']].head()) 

# 3.2.3a - What were the average values for hits, strikeouts, and homeruns? 
print('--------------')
avgs = dfb[['H', 'SO', 'HR']].mean()
print(avgs)

# 3.2.3b - How many times in our data did someone get 150 or more hits and 150 or more strikeouts? 
print('--------------')
count = dfb[(dfb['H'] >= 150) & (dfb['SO'] >= 150)].shape[0]
print(count)

# 3.2.3c - What percent of players who had 150+ hits also had 150+ strikeouts? 
print('--------------')
Hits150 = dfb[dfb['H'] >= 150]
Hits150_Ks150 = Hits150[Hits150['SO'] >= 150]

# Calculate the percentage
percent = (Hits150_Ks150.shape[0] / Hits150.shape[0]) * 100
print(percent)
print('--------------')

# 3.2.3d - What was the MAX number of at bats in our sample? 
max_ABs = dfb['AB'].max()
print(max_ABs)

# 3.2.3e - Find the number of times each team is represented in this dataframe. 
print('--------------')
team_counts = dfb['team'].value_counts()
print(team_counts.reset_index(name='Count').rename(columns={'index': 'Team'}))


