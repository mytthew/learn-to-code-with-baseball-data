#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 20:38:56 2025

@author: matt
"""

# 3.5.1A: 
import pandas as pd
import os

# Set the correct relative path
base_path = '../data/problems/combine1/'
print("Files in folder:", os.listdir(base_path))

# Load the datasets
hits = pd.read_csv(os.path.join(base_path, 'hits.csv'))
outs = pd.read_csv(os.path.join(base_path, 'outs.csv'))
other = pd.read_csv(os.path.join(base_path, 'other.csv'))

# Preview the data
print("\nHits:")
print(hits.head())

print("\nOuts:")
print(outs.head())

print("\nOther:")
print(other.head())

# 3.5.1B: Combine them using pd.merge
# Merge hits and outs on 'batter'
merged_df = pd.merge(hits, outs, on='batter')

# Now merge the result with other on 'batter'
merged_df = pd.merge(merged_df, other, on='batter')

# Show the combined dataset
print(merged_df.head())

# 3.5.1C: Now using pd.concat
# Set 'batter' as the index in each DataFrame
hits = hits.set_index('batter')
outs = outs.set_index('batter')
other = other.set_index('batter')

# Concatenate along columns (axis=1)
combined_df = pd.concat([hits, outs, other], axis=1)

# Reset index to get 'batter' back as a column
combined_df = combined_df.reset_index()

print(combined_df.head())

# 3.5.1C: Which is better? 
# I belive in this scenario pd.merge is better and more efficient because all 3 datasets could be merged on the same column, which is 'batter'.

# 3.5.2A: Load the three datasets in ./data/problems/combine2/. It contains the same data, but split "vertically" in by the defensive position. 
base_path = '../data/problems/combine2/'
print("Files in folder:", os.listdir(base_path))

# Load the datasets
infield = pd.read_csv(os.path.join(base_path, 'infield.csv'))
outfield = pd.read_csv(os.path.join(base_path, 'outfield.csv'))
pitcher = pd.read_csv(os.path.join(base_path, 'pitcher.csv'))

# Preview the data
print("\nInfield:")
print(infield.head())

print("\nOutfield:")
print(outfield.head())

print("\nPitcher:")
print(pitcher.head())

# 3.5.2B: Combine them. Make sure the index of the resulting dataframe is the default (0,1,etc)
combined_df = pd.concat([infield, outfield, pitcher], axis=0).reset_index(drop=True)

# Display the result
print(combined_df.head())

# 3.5.2C: Combine them agan. Now do it so the index is batter. 
combined_df = combined_df.set_index('batter')

# Display the result
print(combined_df.head())

# 3.5.3A: Load the batting data in ./data/2018-season/atbats.csv
file_path = '../data/2018-season/atbats.csv'

# Load the dataset
atbats = pd.read_csv(file_path)

# Preview the data
print(atbats.head())

# 3.5.3B: Write a loop to save subsets of the data frame for each league (AL and NL) to the DATA_DIR.
DATA_DIR = '../data/2018-season/leagues/'
os.makedirs(DATA_DIR, exist_ok=True)

# Loop through each unique league and save to a CSV
for league in atbats['lg'].unique():
    subset = atbats[atbats['lg'] == league]
    file_name = f"{league}.csv"  
    file_path = os.path.join(DATA_DIR, file_name)
    subset.to_csv(file_path, index=False)
    print(f"Saved {league} subset to {file_path}")
    
    
#3.5.3C: Then using pd.concat and list comprehensions, write one line of python that loads these saved subsets and combines them.
combined_df = pd.concat([pd.read_csv(os.path.join(DATA_DIR, f)) for f in os.listdir(DATA_DIR) if f.endswith('.csv')])   
print(combined_df.head())
