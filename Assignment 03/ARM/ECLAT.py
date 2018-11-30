#	ECLAT Algorithm for Association Rule Mining
#		Group 05 - ESD15I018, MFD15I014, CED15I031

""" Outline :  """

import numpy
import csv
from fim import eclat

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

txnDataMale = numpy.asarray (txnDataMale[:1000])
# print ("Male Data")
# print (txnDataMale)

a_rules_male = list (eclat (txnDataMale, target = 'c', supp = -50))

for m_item in a_rules_male: 
	pair = m_item[0]
	m_items = [x for x in pair]
	print (str (m_items))

print ("*************Finished Here with Male Data************\n")

txnDataFemale = numpy.asarray (txnDataFemale[:1000])
# print ("Female Data")
# print (txnDataFemale)

a_rules_female = list (eclat (txnDataFemale, target = 'c', supp = -50))

for f_item in a_rules_female: 
	pair = f_item[0]
	f_items = [x for x in pair]
	print (str (f_items))

print ("*************Finished Here with Female Data************\n")