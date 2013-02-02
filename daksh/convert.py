import pandas as pd
from pandas  import DataFrame
from pandas  import read_csv
from pandas  import Series
import os
import csv
import sys
from pylab import *
import matplotlib
from utils import *


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
	"IMP: Others"]

impListBBMP = [
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
	"IMP: Water Supply and Quality",
	"IMP: Restoration of Lakes",
	"IMP: Functioning of storm water drains and sewerage system",
	"IMP: Trafiic Management",
	"IMP: Encroachment of Public Land, Lakes and Roads",
	"IMP: Parking Facility CD",
	"IMP: Public Facilities I Basic Amenities - Parks, Public Toilets, Quality Footpaths, etc.",
	"IMP: Zoning Regulations",
	"IMP: Others"]


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
	"PERF: Others" ] 

perfListBBMP = [
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
	"PERF: Water Supply and Quality",
	"PERF: Restoration of Lakes",	
	"PERF: Functioning of storm water drains and sewerage system",	
	"PERF: Trafiic Management",	
	"PERF: Encroachment of Public Land, Lakes and Roads",	
	"PERF: Parking Facility CD",	
	"PERF: Public Facilities I Basic Amenities - Parks, Public Toilets, Quality Footpaths, etc.",	
	"PERF: Zoning Regulations",	
	"PERF: Others" ] 

#impList = impListBBMP
#perfList = perfListBBMP

impPerfList = []

for point in range(0, len(impList)):
#	print impList[point], perfList[point]
 	impPerf = impList[point] + "*" + perfList[point]
	impPerfList.append(impPerf)
	df[impPerf] = Series(updatePerf(df[impList[point]], df[perfList[point]]), index=df.index)

updatedFile = filename + "_updated.csv"
#df.to_csv(updatedFile)

scores = {}

from collections import OrderedDict

for point in impPerfList:
	p = point.split("*")[0].split(":")[1].strip()	
	if df[point].count() > 3:
		scores [p] = round(df[point].mean(),2)
	else:
		scores [p] = 0


overallScore = round(getOvelallscore(scores),2)
#print overallScore

report = OrderedDict(sorted(scores.items(), key=lambda x: x[1], reverse=True))

header = "District Name, Name, Party, Candidate Name, MLA's Caste Not Imp. (%), MLA's Caste Imp.(%), MLA's Caste Very Imp.(%),  Accessibility, Trustworthiness, Overall Score, Issue, Score"   + '\n'

line = df.ix[1]
infoList = ['District Name', 'Name', 'Party','Candidate Name']
info = getinfo(line, infoList)


castesImportance=df.groupby('Most important factor to vote: Candidate\'s Caste')
d2 = castesImportanceCount(castesImportance.size())
#print d2
castesImportancePct = calPercentage(d2)

#print report
Accessibility = getKey(report,'Accessibility of MLA/MP')
Trustworthiness = getKey(report, 'Trustworthiness of MLA')
removeKey(report,'Accessibility of MLA/MP')
removeKey(report, 'Trustworthiness of MLA')

#print Accessibility
#print Trustworthiness

firstLine = info['District Name'] + "," + info['Name'] + "," + info['Party'] + "," + info['Candidate Name'] + ',' + str(castesImportancePct['NI']) + ',' +str(castesImportancePct['I']) + ',' +str(castesImportancePct['VI']) +','+ str(Accessibility)  + ',' + str(Trustworthiness) + ',' +str(overallScore) + ',,' + '\n'

titleGraph = "Issues vs Perfomance (Higher is better)"
reportFilename = filename + "_report.xls"
reportFilenameImg = filename + "_top6.png"
writeFile(reportFilename, report, header, firstLine)
genGraph(report, 6, reportFilenameImg, titleGraph)

#lowTohigh = OrderedDict(sorted(d.items(), key=lambda x: x[1]))
#lowTohighFilename = filename + "_lowToigh.csv"
#lowTohighFilenameImg = filename + "_lowToigh.png"
#writeFile(lowTohighFilename, lowTohigh)
#genGraph(lowTohighFilename, 6, lowTohighFilenameImg, titleGraph)

