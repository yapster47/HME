import pandas as pd
import explore_data
import os
import matplotlib.pyplot as plt
import shutil

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
data_loc='../../Downloads/HME_code/hasy/hasyv2/'
data_labels = pd.read_csv(data_loc+"hasy-data-labels.csv") # Note that this is the FULL .csv file (all 168K images)

def prune_column(df, col, lst, out_csv):
    """
    This function takes a dataframe, column name, and list, and returns a dataframe that has removed the rows
    whose column value is NOT within lst.
    Args:
        df: pandas dataframe
        col: column that you're referencing for row removal
        lst: Python list containing column values you want to keep
        out_csv: string
    Returns:
        the new .csv file that removes the data with unwanted labels
        a dataframe with the unwanted data rows removed
        a list of values that is properly inside the set of col values in df
    """

    set_in_df = set(df[col].unique())   #getting the set of col values
    lst = list(set(lst).intersection(set_in_df))  # intersection of col values with given list
    print("Now removing all rows whose value in  ", col, "  is not in ", lst , ".")
    pruned_df=df[df[col].isin(lst)]
    pruned_df.to_csv(out_csv, index=False)
    return out_csv, pruned_df, lst

def subsample(df, col, vals, num_samples, filename='subsample.csv'):
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

    data.to_csv(filename, index=False)
    return data

def check_new_df(path, csvfile, col, count_basis, num_bins):
    """
    This function tests that the new .csv file created is correct and plots the distribution of points over the labels.
    If balanced, the distribution should just be one bar of height = # of labels

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

    print("15 random samples from dataset:\n", data.sample(15))
    print("Counts for each label:\n", print(counts))
    counts.plot.hist(bins=num_bins)
    plt.show()
    return

def create_balanced(source_dir, csvfile, col, dest_dir):
    """
    Takes a dataframe and copies files from source_dir to dest_dir according to the csvfile.

    Args:
        source_dir: string
        csvfile: string
        col: string - name of column containing file names
        dest_dir: string - where to put the files (make sure this directory exists!)

    Returns:
        nothing
    """
    print("Datapath exists: " + str(os.path.exists(source_dir)))
    df=pd.read_csv(csvfile)
    print("Number of files to be copied is: ", df[col].shape)
    files = list(df[col])
    for file in files:
        f= source_dir+file
        if os.path.exists(f):
            shutil.copy(f, dest_dir)
        else:
            print("f" + "does not exist")
    print("Files in" + dest_dir + ": \n ", os.listdir(dest_dir))
    return



if __name__ == '__main__':
    symbols = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'x',
               '0', '+','\\div','\\sqrt{}', '-', '\\cdot',
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
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
               '\\pi', '\\alpha', '\\beta', '\\sum', '\\sigma', '\\Sigma', '\\gamma',
               '\\Gamma', '\\delta', '\\Delta', '\\zeta', '\\eta', '\\theta',
               '\\epsilon', '\\iota', '\\kappa',
               '\\lambda', '\\Lambda', '\\mu', '\\nu', '\\xi',
               '\\Pi', '\\rho', '\\tau', '\\phi', '\\nabla',
               '\\chi', '\\psi', '\\omega', '\\Omega']

    data_loc = '../../Downloads/HME_code/hasy/hasyv2/'

    csvfile =  "hasy-data-labels.csv"  # Note that this is the FULL .csv file (all 168K images)

    data= explore_data.get_df(data_loc,csvfile)

    data= explore_data.modify_col_data(data,'path', 'hasy-data/', '', True)

    data, vals = prune_column(data, 'latex', symbols[0:17])

    uniform_data = subsample(data, 'latex', vals, num_samples=50, filename='subset.csv')

    check_new_df('./', 'subset.csv', 'latex', 'path', num_bins=20)

######################################
    balanced_file = "balanced.csv"
    data_path = '../../Downloads/HME_code/hasy/hasyv2/'
    source = 'hasyv2-data/'
    destination_directory = data_path + 'hasyv2-balanced-subset'

    create_balanced(data_path + source, balanced_file, 'path', destination_directory)