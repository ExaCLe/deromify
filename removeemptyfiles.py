# Opens files in directory and deletes them if they are empty.

import re
import glob
import os

# get the valutDir from the environment variable
vaultDir = os.environ['VAULTDIR']

files = os.listdir(vaultDir)

for file in files:
    # print(file)
    # check if size of file is 0
    if os.stat(vaultDir + file).st_size == 0:
        os.remove(vaultDir + file)
        print(file)

