import pandas as pd
import matplotlib.pyplot as plt

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



def get_df(dirpath,filename):
    """ Locates and then converts a .csv file into a pandas dataframe
    Args:
        dirpath: string
        filename: string

    Returns:
        data (pandas dataframe)
    """
    data = pd.read_csv(dirpath+filename)
    print("Opening ", filename, "as dataframe.")
    return data

def modify_col_data(df,colname, to_delete, replace_with, reg):
    """ Modifies string entries of dataframe.
    Args:
        df (pandas dataframe):
        colname (string): name of column to be modified
        to_delete(string): string to be removed
        replace_with (string): string to replace
        reg (Bool): see https://www.programiz.com/python-programming/regex to compare regex with raw text
    Returns (pandas dataframe): modified dataframe
    """
    df[colname]=df[colname].str.replace(to_delete, replace_with, regex=reg)
    return df


#Let's see how balanced/imbalanced the data is
def label_counts(df, col_name, points, num_bins, norm=False):
    """
    Checking if your data is imbalanced.
    Gets the unique labels of the (categorical) data and counts how frequently each labels appears.
    Also plots the distribution (histogram) of points across labels

    Args:
        df (pandas dataframe)
        col_name (string): name of label column
        num_bins (int): how many bins you want to see in histogram
        norm (Bool): If True, gives relative frequencies of the unique values
        points (string): column that holds filename (or other identifier) of data point
    Returns:
        Series containing unique values
        Series containing value counts for each unique value
        Groupby object with one dataframe per label
    """
    print("Number of unique labels of the data:",len(df[col_name].unique()))
    print("The Series of unique labels:",df[col_name].unique())
    print("The distribution of data points across the labels: ", df[col_name].value_counts(normalize=norm))
    lab_counts=df.groupby(col_name)[points].count()
    lab_counts.plot.hist(bins=num_bins)
    plt.show()

    return df[col_name].unique(), df[col_name].value_counts(normalize=norm), df.groupby(col_name)

if __name__=='__main__':

    data_labels= get_df('../../Downloads/HME_code/hasy/hasyv2/','hasy-data-labels.csv')
    data_labels= modify_col_data(data_labels,'path', 'hasy-data/', '', True)
    A, B, C = label_counts(data_labels, 'latex', 'path', 80, False)
    '''for sym, frame in C:
        print(sym)
        print(frame.head(1))
    '''
    print(get_df.__doc__)