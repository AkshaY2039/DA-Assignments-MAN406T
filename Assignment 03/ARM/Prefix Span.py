#	Prefix Span Algorithm for Association Rule Mining
#		Group 05 - ESD15I018, MFD15I014, CED15I031

""" Outline :  """

import numpy
import csv
from pyprefixspan import pyprefixspan

txnDataMale = []
txnDataFemale = []

# Loading Data
print ("Data Loading Started"), 
with open ('../../Dataset/Generated Data Set/daily smoking times.csv') as csvdata: 
	readCSV = csv.reader (csvdata, delimiter=',')
	next (readCSV)	# Skipping Header content
	for row in readCSV: 
		try: 
			if (row[0] == 'M'): 
				values = row[2:7]
				txnDataMale.append (numpy.asarray (values))
			else: 
				values = row[2:7]
				txnDataFemale.append (numpy.asarray (values))
		except ValueError: 
			pass
print ("Done Loading Data\n")

txnDataMale = numpy.asarray (txnDataMale)
# print ("Male Data")
# print (txnDataMale)

rules_male = pyprefixspan (txnDataMale)
rules_male.run ()
rules_male.out

print ("*************Finished Here with Male Data************\n")

txnDataFemale = numpy.asarray (txnDataFemale)
# print ("Female Data")
# print (txnDataFemale)

rules_female = pyprefixspan (txnDataFemale)
rules_female.run ()
rules_female.out

print ("*************Finished Here with Female Data************\n")