import pandas as pd
from pandas  import DataFrame
from pandas  import read_csv
import os
import sys


csvFileAllMla = sys.argv[1]
splitBy = sys.argv[2]
dirForOutput = sys.argv[3]


data = read_csv(csvFileAllMla)

df = DataFrame(data)

gSplitby = df.groupby(splitBy)

for splitBy,group in gSplitby:
	splitBy = splitBy.replace(" ", "_")
	path = os.path.join(dirForOutput, splitBy)
	os.makedirs(path)
	filename = os.path.join(path, splitBy)
	filename = filename.replace(" ", "_")
	group.to_csv(filename)
	cmd = "python convert.py" + " " + str(filename)
	os.system(cmd)
