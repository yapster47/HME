import pandas as pd
import os
import shutil
import explore_data
import keep_subset

import numpy as np

import random



# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#os.chdir('../../Downloads/HME_code/hasy/hasyv2')

# 1.) Decide on labels you want to keep
# 2.) Explore distribution of data across those labels (ie/check for balance)
# 3.) Create new .csv file for label subset
# 4.) If necessary (b/c of space considerations), create new folder of data containing only the
#     points in data set

symbols = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'x',
           '0', '+', '\\div', '\\sqrt{}', '-', '\\cdot',
           '\\angle',
           '\\approx', '\\sim', '\\equiv', '\\neq',
           '\\int', '\\iint', '\\oint', '\\cdot', '\\leq', '\\geq', '<', '>',
           '\\subset', '\\supset', '\\subseteq', '\\supseteq', '\\cong',
           '\\propto', '-', '+', '\\$', '\\{',
           '\\dots', '\\checkmark', '\\pm', '\\bullet', '\\setminus',
           '\\circ', '\\star', '\\approx', '\\equiv', '\\not\\equiv',
           '\\parallel', '\\lor', '\\land',
           '\\downarrow', '\\rightarrow', '\\leftarrow', '\\neq', '\\neg', '\\infty', '\\prime',
           '\\angle',
           '\\triangle', '\\square', '\\sim', '\\doteq', '\\parallel', '\\langle', '\\rangle',
           'a', 'b', 'c',
           'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           '\\pi', '\\alpha', '\\beta', '\\sum', '\\sigma', '\\Sigma', '\\gamma',
           '\\Gamma', '\\delta', '\\Delta', '\\zeta', '\\eta', '\\theta',
           '\\epsilon', '\\iota', '\\kappa',
           '\\lambda', '\\Lambda', '\\mu', '\\nu', '\\xi',
           '\\Pi', '\\rho', '\\tau', '\\phi', '\\nabla',
           '\\chi', '\\psi', '\\omega', '\\Omega']

# df is the new dataframe with only the labels you want to keep and kept_lbls is the list
data_loc = '../../Downloads/HME_code/hasy/hasyv2/'

csvfile = "hasy-data-labels.csv"  # Note that this is the FULL .csv file (all 168K images)

labels='latex'

# get the initial dataframe
df = explore_data.get_df(data_loc, csvfile)
# remove directory name from 'path column
df = explore_data.modify_col_data(df, 'path', 'hasy-data/', '', True)
# prunt according to the given list of symbols
pruned_csv, pruned_df, kept_lbls = keep_subset.prune_column(df, 'latex', symbols[0:17], 'pruned.csv')
# plot distribution of pruned dataset
keep_subset.check_new_df('./',  pruned_csv, labels, 'path', num_bins=100)

