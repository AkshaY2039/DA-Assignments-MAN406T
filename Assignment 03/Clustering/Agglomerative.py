#	Agglomerative Algorithm for Clustering
#		Group 05 - ESD15I018, MFD15I014, CED15I031

""" Outline :  """

import numpy
import csv
from matplotlib import pyplot
from sklearn.cluster import AgglomerativeClustering

dataAttributes = []

Attributes = {
	"2": {},	# Year
	"3": {},	# 70+ years old (deaths)
	"4": {},	# 5-14 years old (deaths)
	"5": {},	# 15-49 years old (deaths)
	"6": {},	# 50-69 years old (deaths)
	"7": {}		# Under-5s (deaths)
}

# Year vs 70+ years old death
entityIndex = [2,3]

# Loading Data
print ("Data Loading Started"), 
with open ('../../Dataset/secondhand-smoke-deaths-by-age.csv') as csvdata: 
	readCSV = csv.reader (csvdata, delimiter=',')
	next (readCSV)	# Skipping Header content
	for row in readCSV: 
		for i in entityIndex: 
			if (row[i] in Attributes[str (i)]) == False: 
				Attributes[str (i)][row[i]] = len (Attributes[str (i)].keys())
		datarow = []
		try: 
			values = row[3]
			# pValues = []
			# for value in values: 
			# 	pValues.append (Attributes[str (3)][value])
			# p = numpy.sum (pValues) / len (values)
			# datarow.append (p)
			datarow.append (values)
			dataAttributes.append (numpy.asarray (datarow))
		except ValueError: 
			pass
feats = ["Year","70+ years old (deaths)"]

print ("Features: ", feats)

print ("Done Loading Data\n")

# seperating test and training data
dataAttributes = numpy.asarray (dataAttributes)

print ("Agglomerative Clustering Started")
linkage = "ward" # ward minimizes the variance of the clusters being merged
AggCluster = AgglomerativeClustering (linkage = linkage, n_clusters = 5).fit (dataAttributes)
print ("Agglomerative Clustering Finished\n")

pyplot.scatter (dataAttributes.T[0], dataAttributes.T[1], c = clustering.labels_)
pyplot.show ()
