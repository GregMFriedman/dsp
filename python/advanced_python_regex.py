# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 20:07:26 2015

@author: gregoryfriedman
"""

import pandas as pd
import numpy as np

####Q1. Find how many different degrees there are, 
# and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

fd = pd.read_csv('faculty.csv')

fd['degree'] = fd[' degree'].str.replace('.','').str.lower()
#print fd['degree']

#phds = len(fd[fd.degree.str.contains('phd')])
#print phds

degree_list = np.array(fd['degree'])
#print degree_list
degrees = []
for entry in degree_list:
    degrees.append(entry.split())
#print degrees

total_degrees = []
for entry in degrees:
    for i in range(len(entry)):
        total_degrees.append(entry[i])

#print total_degrees

def count_degrees(degreelist):
    degree_count = {}
    for degree in degreelist:
        if degree in degree_count:
            degree_count[degree] += 1
        else:
            degree_count[degree] = 1
    return degree_count

degree_tally = count_degrees(total_degrees)
print degree_tally
print len(degree_tally) 
    
#There are 8 types of degrees and the tally of each is stored in the variable
#"degree_tally".  The ninth key in degree_tally is that of the one person that
#has no degrees.
    

####Q2. Find how many different titles there are, and their frequencies:  
#Ex:  Assistant Professor, Professor

#print fd

titles = np.array(fd[' title'])
#print titles

def count_titles(titlelist):
    title_count = {}
    for title in titlelist:
        if title in title_count:
            title_count[title] += 1
        else:
            title_count[title] = 1
    return title_count

print count_titles(titles)

#There are 3 titles, 12  Asst Prof's, 13 Prof's & 12 Associate Prof's

emails = np.array(fd[' email'])
print emails

domains = []
for email in emails:
    at = email.find('@')
    domains.append(email[at+1:])

#print domains

domain_count = {}
def count_domain_types(domain_list):
    for domain in domain_list:
        if domain in domain_count:
            domain_count[domain] += 1
        else:
            domain_count[domain] = 1
    return domain_count

#print count_domain_types(domains)

domain_types = count_domain_types(domains)

for key in domain_types:
    print key