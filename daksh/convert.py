import pandas as pd
from pandas  import DataFrame
from pandas  import read_csv
from pandas  import Series
import sys
import os


def changeImp(val):
	if val == 'L':
		val = 1
	if val == 'M':
		val = 2
	if val == 'H':
		val = 3
	if val == 'L-M':
		val = 2
	if val == 'M-H':
		val = 3
	if val == 'L-H':
		val = 3
	if val == 'L-M-H':
		val = 3
	return val

def changePerf(val):
	if val == 'B':
		val = 1
	if val == 'A':
		val = 2
	if val == 'G':
		val = 3
	if val == 'B-A':
		val = 2
	if val == 'A-G':
		val = 3
	if val == 'B-G':
		val = 3
	if val == 'B-A-G':
		val = 3
	return val


def updatePerf(imp, perf):
	imp = imp.apply(changeImp)
	perf = perf.apply(changePerf)
	return imp * perf


filename = sys.argv[1]
print filename
data = read_csv(filename)
df = DataFrame(data)


impList = ["IMP: Easier access to drinking water",
	"IMP: Free Electricity",
	"IMP: Free/Subsidized Loans",	
	"IMP: Support for Economically-weaker Sections",
	"IMP: Irrigation Programs",
	"IMP: Jobs through rural employment schemes",	
	"IMP: Lower rice/wheat prices",
	"IMP: More schools",
	"IMP: More teachers",
	"IMP: School Facilities",
	"IMP: Subsidy for seeds/fertilizers",
	"IMP: Accessibility of MLA/MP",
	"IMP: Better Law and Order/Policing",
	"IMP: Better Public Transport",
	"IMP: Better Roads",
	"IMP: Eradication of Corruption",
	"IMP: More Hospitals/Primary Health Care Centers",
	"IMP: Trustworthiness of MLA",
	"IMP: Security for Women",
	"IMP: Better Electric Supply",	
	"IMP: Better Employment Opportunities",	
	"IMP: Better Garbage Clearance",
	"IMP: Reservation for Jobs and Education",
	"IMP: Subsidized Food Distribution",
	"IMP: Training for Jobs",
	"PERF: Others"]

perfList = ["PERF: Easier access to drinking water",
	"PERF: Free Electricity",
	"PERF: Free/Subsidized Loans",
	"PERF: Support for Economically-weaker Sections",
	"PERF: Irrigation Programs",
	"PERF: Jobs through rural employment schemes",
	"PERF: Lower rice/wheat prices",
	"PERF: More schools",
	"PERF: More teachers",
	"PERF: School Facilities",
	"PERF: Subsidy for seeds/fertilizers",
	"PERF: Accessibility of MLA/MP",
	"PERF: Better Law and Order/Policing",
	"PERF: Better Public Transport",
	"PERF: Better Roads",
	"PERF: Eradication of Corruption",
	"PERF: More Hospitals/Primary Health Care Centers",
	"PERF: Trustworthiness of MLA",
	"PERF: Security for Women",
	"PERF: Better Electric Supply",
	"PERF: Better Employment Opportunities",
	"PERF: Better Garbage Clearance",
	"PERF: Reservation for Jobs and Education",	
	"PERF: Subsidized Food Distribution",
	"PERF: Training for Jobs",
	"PERF: Others.1" ] 

#print len(impList)
#print len(perfList)

impPerfList = []

for point in range(0, len(impList)):
#	print impList[point], perfList[point]
 	impPerf = impList[point] + "*" + perfList[point]
	impPerfList.append(impPerf)
	df[impPerf] = Series(updatePerf(df[impList[point]], df[perfList[point]]), index=df.index)

updatedFile = filename + "_updated.csv"
print updatedFile
df.to_csv(updatedFile)

d = {}

from collections import OrderedDict

for point in impPerfList:
	p = point.split("*")[0].split(":")[1].strip()	
	d [p] = df[point].mean()

highToLow = OrderedDict(sorted(d.items(), key=lambda x: x[1], reverse=True))
lowTohigh = OrderedDict(sorted(d.items(), key=lambda x: x[1]))

print highToLow
print lowTohigh 

highToLowFilename = filename + "_highToLow.csv"
lowTohighFilename = filename + "_lowToigh.csv"

with open(highToLowFilename,'wb') as f: 
	header = "issue" + "," + "score" + "\n"
	f.write(header)
	for key in highToLow.keys():
		line = key + "," + str(highToLow[key]) + "\n"
		f.write(line)
	f.close()

with open(lowTohighFilename,'wb') as f: 
	header = "issue" + "," + "score" + "\n"
	f.write(header)
	for key in lowTohigh.keys():
		line = key + "," + str(lowTohigh[key]) + "\n"
		f.write(line)
	f.close()
