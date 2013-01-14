import pandas as pd
from pandas  import DataFrame
from pandas  import read_csv
import os
import sys


csvFileAllMla = sys.argv[1]
outFile = sys.argv[2]

def ageBucket(x):
        if x < 18:
            bucket = "Below 19"
        elif x >= 18 and x <= 28:
            bucket = "Between 18 and 28"
        elif x >= 29 and x <= 38:
            bucket = "Between 29 and 38"
        elif x >= 39 and x <= 48:
            bucket = "Between 39 and 48"
        elif x >= 49 and x <= 58:
            bucket = "Between 49 and 58"
        elif x >= 59 and x <= 68:
            bucket = "Between 59 and 68"
        elif x >= 69 and x <= 78:
            bucket = "Between 69 and 78"
        elif x > 78:
            bucket = "above 78"
        elif x:
            bucket = x

        return bucket

data = read_csv(csvFileAllMla)

df = DataFrame(data)
df['Age Bucket'] = df['Age'].apply(ageBucket)

df.to_csv(outFile)
