# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 10:12:49 2015

@author: gregoryfriedman
"""

import pandas as pd
#import numpy as np

fd = pd.read_csv('faculty.csv')
fd[' email'].to_csv('emails.csv', index = False)
print pd.read_csv('emails.csv')