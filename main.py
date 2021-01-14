import pandas as pd
import os
import shutil
import explore_data
import keep_subset
l
import numpy as np

import random



# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

data_labels = pd.read_csv("balanced.csv") # Note that this is the FULL .csv file (all 168K images)

images=list(data_labels['path'])
#subsample=random.sample(images,10000)

print("Number of images from smaller Latex list: ",len(images) )

os.chdir('../../Downloads/HME_code/hasy/hasyv2')

for f in images:
    print("File exists:" + str(os.path.exists('hasyv2-data/'+f)))
    print('hasyv2-data/'+f)
    if os.path.exists('hasyv2-data/' + f):
        shutil.copy('hasyv2-data/' + f, "hasyv2-symbol-subset")
    #print(data_loc+'hasyv2-data/'+f)
    #shutil.copy(data_loc+'hasyv2-data/'+f, 'hasyv2-symbol-subset')

#print(os.getcwd())
#os.chdir('../../Downloads/HME_code/hasy/hasyv2')
#print(os.getcwd())
print(os.listdir("hasyv2-symbol-subset"))
#os.mkdir('hasyv2-symbol-subset')
# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
