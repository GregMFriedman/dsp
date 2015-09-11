# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 10:37:36 2015

@author: gregoryfriedman
"""

import pandas as pd
from operator import itemgetter

fd = pd.read_csv('faculty.csv')

fd_list = map(list, fd.values)
#print fd_list

for entry in fd_list:
    title_end = entry[2].find("Professor") + 9
    entry[2] = entry[2][:title_end]
    entry[0] = entry[0].split()

#print fd_list

faculty_dict = {}
for entry in fd_list:
    last = entry[0][len(entry[0])-1]
    if last not in faculty_dict:
        faculty_dict[last] = entry[1:]
    elif len(faculty_dict[last]) == 3:
        first, faculty_dict[last] = faculty_dict[last], []
        faculty_dict[last].append(first)
        faculty_dict[last].append(entry[1:])
    else:
        faculty_dict[last].append(entry[1:])

        
#print faculty_dict
    
#print faculty_dict.items()[:3]

faculty_sort = sorted(faculty_dict)
for key in faculty_sort[:3]:
    print (key, faculty_dict[key])

#print fd_list
for entry in fd_list:
    entry[0] = tuple(entry[0])

#print fd_list

professor_dict = {}
for entry in fd_list:
    professor_dict[entry[0]] = entry[1:]

#print professor_dict

firsts = sorted(professor_dict)

for key in firsts[:3]:
    print (key, professor_dict[key])

surnames = sorted(professor_dict, key=itemgetter(-1,0))

for key in surnames[:3]:
    print (key, professor_dict[key])