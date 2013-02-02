import pandas as pd
from pandas  import DataFrame
from pandas  import read_csv
from pandas  import Series
import os
import csv
import sys
from pylab import *
import matplotlib

def genGraph(report, topn, imageFilename, titleGraph):
    issues = report.keys()
    ratings = report.values()
    labels = issues[0:topn] # take top n values
    data =   ratings[0:topn]
    x = arange(1, len(data)+1)
    colour = ['#373737', '#696969','#989898','#CDCDCD','#D2D2D2', '#e6e6e6']
    fig = plt.figure()
    fig.subplots_adjust(right=0.7)
    ax = plt.subplot(111)
    box = ax.get_position()
    title(titleGraph)
    ax.set_position([box.x0, box.y0, box.width , box.height])
    ax.bar(x, data,color=colour)
    ax.set_xticklabels(labels, rotation=90,ha='center',size='small')
#    legend(labels,prop={'size':8}, loc='center', bbox_to_anchor=(1.4,0.8))
    ax.set_xlabel("Issues")
    ax.set_ylabel("Score (out of 10)")
#    plt.show()
    plt.savefig(imageFilename, bbox_inches='tight')

def changeImp(val):
	if val == 'LOW':
		val = 1
	if val == 'MEDIUM':
		val = 2
	if val == 'HIGH':
		val = 3
	if val == 'LOW-MEDIUM':
		val = 2
	if val == 'MEDIUM-HIGH':
		val = 3
	if val == 'LOW-HIGH':
		val = 3
	if val == 'LOW-MEDIUM-HIGH':
		val = 3
	return val

def changePerf(val):
	if val == 'BAD':
		val = 1
	if val == 'AVERAGE':
		val = 2
	if val == 'GOOD':
		val = 3
	if val == 'BAD-AVERAGE':
		val = 2
	if val == 'AVERAGE-GOOD':
		val = 3
	if val == 'BAD-GOOD':
		val = 3
	if val == 'BAD-AVERAGE-GOOD':
		val = 3
	return val

def normalize(x):
	A = 1.0
	B = 9.0	
	a = 1.0
	b = 10.0
	norm = a + (((x - A) * ( b - a))/(B - A))
	return norm

def updatePerf(imp, perf):
	imp = imp.apply(changeImp)
	perf = perf.apply(changePerf)
	#print imp
	#print perf
	norm = normalize(imp * perf)
	return norm

def writeFile(filename, odict, header, firstLine):
	with open('/tmp/All.xls','a') as f1: 
		with open(filename,'wb') as f: 
			f.write(header)
			f.write(firstLine)
			f1.write(firstLine)
			for key in odict.keys():
				line = ",,,,,,,,,," +key + "," + str(odict[key]) + "\n"
				f.write(line)
			f.close()
		f1.close()

def getKey(odict, key):
	return  odict[key]

def removeKey(odict, key):
	odict = odict.pop(key)
	return odict 

def getinfo(series, l):
	d = {}
	for item in l:
		#print series[item]
		d[item] = series[item]
	return d

def getOvelallscore(scores):
#	print scores
	overallScore = sum(scores.values())
	count = 0
	for s in scores.values():
		if s > 0:
			count = count + 1
#	print count
	issues = len(scores.keys())
#	overallScore = overallScore / issues
	overallScore = overallScore / count
	return overallScore
		
def castesImportanceCount(castesImportance):
	d = {}
	l1 = ['NI', 'I', 'VI']
	set1 = set(l1)
	set2 = set(castesImportance.keys())
	for key in castesImportance.keys():
		#print castesImportance[key]
		d [key] = castesImportance[key]
	diff = set.difference(set1, set2)
	for i in diff:
		d[i] = 0
	return d

def calPercentage(d):
	total = sum(d.values())
	#print total 
	for key in d.keys():
		val = float(d[key])
		pct = (val/total) * 100
		d[key] = round(pct)
	return d
	
	
