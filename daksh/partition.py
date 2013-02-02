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
	path = path.replace("(", "[")
	path = path.replace(")", "]")
	os.makedirs(path)
	filename = os.path.join(path, splitBy)
	filename = filename.replace(" ", "_")
	filename = filename.replace("(", "[")
	filename = filename.replace(")", "]")
	group.to_csv(filename)
	cmd = "python convert.py" + " " + filename
	os.system(cmd)
	cmd = 'rm -rf ' + filename
	os.system(cmd)
