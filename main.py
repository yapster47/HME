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

balanced_file="balanced.csv"
data_path='../../Downloads/HME_code/hasy/hasyv2/'
source= 'hasyv2-data/'
destination_directory= data_path +'hasyv2-balanced-subset'

create_balanced(data_path+source, balanced_file,'path',  destination_directory)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
