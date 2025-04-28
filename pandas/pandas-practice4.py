#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 08:46:02 2025

@author: matt
"""

# 3.3.1 - Load the pitcher data form ./data/2018-season/pitches.csv into a Dataframe named dfp.  
import pandas as pd
from os import path
import os

DATA_DIR = '/Users/matt/Desktop/learn-to-code-with-baseball-data/data'

dfp = pd.read_csv(
    path.join(DATA_DIR, '2018-season', 'pitches.csv'))

print(dfp.head())

# 3.3.2 - Make a smaller Dataframe with just Yankees pitchers and only the columns: 'nameFirst', 'nameLast', 'G', 'ERA'. 
# Do it two ways: 1) using the loc syntax, and 2) using the query syntax. Call them dfp_nyy1  and dfp_nyy2
# Loc Syntax:
dfp_nyy1 = dfp.loc[
    (dfp['teamID'] == 'NYA'),
    ['nameFirst', 'nameLast', 'G', 'ERA']]
print(dfp_nyy1.head())

# Query Syntax: 
dfp_nyy2 = dfp.query("teamID == 'NYA'")[['nameFirst', 'nameLast', 'G', 'ERA']]
print(dfp_nyy2.head())

# 3.3.3 - Make a dataframe 'dfp_no_nyy' with the same columns that is everyone EXCEPT yankee players, and add the 'teamID' column to it. 
dfp_no_nyy  = dfp.loc[
    dfp['teamID'] != 'NYA',
    ['nameFirst', 'nameLast', 'G', 'ERA', 'teamID']]
print(dfp_no_nyy.head())

# 3.3.4a - Are there any duplicates by last name AND league (AL or NL) in our dfp dataframe? How many? 
duplicates = dfp.duplicated(subset=['nameLast', 'lgID'], keep=False)
dfp_duplicates = dfp[duplicates]

# Count the number of duplicated rows
num_duplicates = dfp_duplicates.shape[0]
print(num_duplicates)

# 3.3.4b - Divide dfp into two  seperate dataframes 'dfp_dups' and 'dfp_nodups', one with dups (from previous Q) and one without. 
dfp_dups = dfp[duplicates]
print(dfp_dups.head())

dfp_nodups = dfp[~duplicates]
print(dfp_nodups.head())

# 3.3.5 - Add a new column to dfp called 'era_Description' with the values: 'stud' for players with an ERA  2.5 or under, 'scrub' for ERA's over 5, and 'missing' otherwise. 
dfp['era_Description'] = 'missing'  
dfp.loc[dfp['ERA'] <= 2.5, 'era_Description'] = 'stud'
dfp.loc[dfp['ERA'] > 5, 'era_Description'] = 'scrub'

# Check if it worked
print(dfp[['nameFirst', 'nameLast', 'teamID', 'ERA', 'era_Description']].head())

# 3.3.6 - Make a new dataframe with only observations for which 'era_descritpion' is missing. Do it with both the loc and syntax methods. 
dfp_no_desc1 = dfp.loc[dfp['era_Description'] == 'missing']
print(dfp_no_desc1.head())

dfp_no_desc2 = dfp[dfp['era_Description'] == 'missing']
print(dfp_no_desc2.head())















