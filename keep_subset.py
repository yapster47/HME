import pandas as pd
import explore_data

import matplotlib.pyplot as plt
import os
import shutil
import random


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
data_loc='../../Downloads/HME_code/hasy/hasyv2/'
data_labels = pd.read_csv(data_loc+"hasy-data-labels.csv") # Note that this is the FULL .csv file (all 168K images)

def prune_column(df, col, lst):
    """
    This function takes a dataframe, column name, and list, and returns a dataframe that has removed the rows
    whose column value is NOT within lst.
    Args:
        df: pandas dataframe
        col: column that you're referencing for row removal
        lst: Python list containing column values you want to keep

    Returns:
        a dataframe with the unwanted data rows removed
        a list of values that is properly inside the set of col values in df
    """
    set_in_df = set(df[col].unique())   #getting the set of col values
    lst = list(set(lst).intersection(set_in_df))  # intersection of col values with given list
    print("Now removing all rows whose value in  ", col, "  is not in ", lst , ".")

    return df[df[col].isin(lst)], lst

def subsample(df, col, vals, num_samples, filename='balanced.csv'):
    """
    Uniformly subsamples an equal number of data points for each unique label in col.
    Also exports new dataframe to filename

    Args:
        df:
        col:
        vals:
        samples:

    Returns:
        modified dataframe containing data uniformly distributed across labels
    """
    data = pd.DataFrame(columns=df.columns)  #create new, empty dataframe
    print("new empty dataframe cols are: ", data.columns)
    for val in vals:
        try:
            df_temp=df[df[col] == val].sample(num_samples)
            data=data.append(df_temp)
        except:
            print("no data for the value ", val)
            continue
    #counts=df.groupby(col)[points].count()

    data.to_csv(filename)
    return data

def check_new_df(path, csvfile, col, count_basis, num_bins):
    """
    This function tests that the new .csv file created is correct and plots the distribution of points over the labels.
    The distribution should just be one bar of height = # of labels
    Args:
        csvfile: string
        col: string
        num_bins: int

    Returns:
        Nothing; only plots and gives data about new dataframe

    """
    data=explore_data.get_df(path,csvfile)
    #counts = data.groupby(col)[points].count()
    counts = data.groupby(col)[count_basis].count()
    print(data.sample(15))
    print(data.describe)
    counts.plot.hist()
    plt.show()
    return



if __name__ == '__main__':
    symbols = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c',
               'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
               '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
               '\\pi', '\\alpha', '\\beta', '\\sum', '\\sigma', '\\Sigma', '\\gamma',
               '\\Gamma', '\\delta', '\\Delta', '\\zeta', '\\eta', '\\theta',
               '\\epsilon', '\\iota', '\\kappa',
               '\\lambda', '\\Lambda', '\\mu', '\\nu', '\\xi',
               '\\Pi', '\\rho', '\\tau', '\\phi', '\\nabla',
               '\\chi', '\\psi', '\\omega', '\\Omega', '\\approx', '\\sim', '\\equiv', '\\neq',
               '\\int', '\\iint', '\\oint', '\\cdot', '\\leq', '\\geq', '<', '>',
               '\\subset', '\\supset', '\\subseteq', '\\supseteq', '\\cong',
               '\\propto', '-', '+', '\\$', '\\{',
               '\\dots', '\\checkmark', '\\pm', '\\div', '\\bullet', '\\setminus',
               '\\circ', '\\star', '\\approx', '\\equiv', '\\not\\equiv',
               '\\parallel', '\\lor', '\\land',
               '\\downarrow', '\\rightarrow', '\\leftarrow', '\\neq', '\\sqrt{}', '\\neg', '\\infty', '\\prime',
               '\\angle',
               '\\triangle', '\\square', '\\sim', '\\doteq', '\\parallel', '\\langle', '\\rangle']

    data_loc = '../../Downloads/HME_code/hasy/hasyv2/'

    csvfile =  "hasy-data-labels.csv"  # Note that this is the FULL .csv file (all 168K images)

    data= explore_data.get_df(data_loc,csvfile)

    data= explore_data.modify_col_data(data,'path', 'hasy-data/', '', True)

    data, vals = prune_column(data, 'latex', symbols)

    uniform_data = subsample(data, 'latex', vals, num_samples=50, filename='balanced.csv')

    check_new_df('./', 'balanced.csv', 'latex', 'path', num_bins=20)