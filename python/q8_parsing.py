#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.


# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 09:57:44 2015

@author: gregoryfriedman
"""

import pandas

def read_data(data):
    return pandas.read_csv(data)

#print read_data('football.csv')
pd = read_data('football.csv')

def get_min_score_difference(pd):
    pd['Score_Difference'] = pd['Goals'] - pd['Goals Allowed']
    pd['Absolute_Difference'] = abs(pd['Score_Difference'])
    gd = pd.loc[:,['Team','Score_Difference', 'Absolute_Difference']]
    return gd

#print get_min_score_difference(pd)
gd = get_min_score_difference(pd)

def get_team(gd, view):
    closest = gd.sort(columns='Absolute_Difference')
    return closest[0: view]

print get_team(gd, 1)