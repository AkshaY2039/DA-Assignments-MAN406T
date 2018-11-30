#	Frequent Pattern Algorithm for Association Rule Mining
#		Group 05 - ESD15I018, MFD15I014, CED15I031

""" Outline :  """

import numpy
import csv
import pyfpgrowth

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

m_patterns = pyfpgrowth.find_frequent_patterns (txnDataMale, 50)
rules_male = pyfpgrowth.generate_association_rules (m_patterns, 0.60)

for m_item in rules_male: 
	print (m_item)

print ("*************Finished Here with Male Data************\n")

txnDataFemale = numpy.asarray (txnDataFemale)
# print ("Female Data")
# print (txnDataFemale)

f_patterns = pyfpgrowth.find_frequent_patterns (txnDataFemale, 55)
rules_female = pyfpgrowth.generate_association_rules (f_patterns, 0.60)

for f_item in rules_female: 
	print (f_item)

print ("*************Finished Here with Female Data************\n")