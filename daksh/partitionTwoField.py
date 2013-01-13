import pandas as pd
from pandas  import DataFrame
from pandas  import read_csv
import os
import sys


csvFileAllMla = sys.argv[1]
splitBy = sys.argv[2]
dirForOutput = sys.argv[3]

l = splitBy.split(",") 
print l


data = read_csv(csvFileAllMla)

df = DataFrame(data)

gSplitby = df.groupby(l)

for splitBy,group in gSplitby:
	firstLevel = splitBy[0]
	firstLevel = firstLevel.replace(" ", "_")
	secondLevel = l[1].replace(" ", "_")
	path = os.path.join(dirForOutput, firstLevel, secondLevel, splitBy[1])
	os.makedirs(path)
	filename = os.path.join(path, splitBy[0])
	filename = filename.replace(" ", "_")
	group.to_csv(filename)
	cmd = "python convert.py" + " " + str(filename)
	os.system(cmd)
