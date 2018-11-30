#	Agglomerative Algorithm for Clustering
#		Group 05 - ESD15I018, MFD15I014, CED15I031

""" Outline :  """

import numpy
import csv
from matplotlib import pyplot
from sklearn.cluster import AgglomerativeClustering

dataAttributes = []

Attributes = {
	"0": {},	# Gender
	"1": {},	# age
	"2": {},	# Time Slot 1
	"3": {},	# Time Slot 2
	"4": {},	# Time Slot 3
	"5": {},	# Time Slot 4
	"6": {},	# Time Slot 5
	"7": {},	# Time Slot 6
	"8": {}		# Time Slot 7
}

# age and smoking hour in night
entityIndex = [1,8]

# Loading Data
print ("Data Loading Started"), 
with open ('../../Dataset/Generated Data Set/daily smoking times.csv') as csvdata: 
	readCSV = csv.reader (csvdata, delimiter=',')
	next (readCSV)	# Skipping Header content
	for row in readCSV: 
		for i in entityIndex: 
			if (row[i] in Attributes[str (i)]) == False: 
				Attributes[str (i)][row[i]] = len (Attributes[str (i)].keys())
		datarow = []
		try: 
			for i in entityIndex: 
				datarow.append (Attributes[str (i)][row[i]])
			dataAttributes.append (numpy.asarray (datarow))
		except ValueError: 
			pass
feats = ["Age","TimeSlot(0-3)"]

print ("Features: ", feats)

print ("Done Loading Data\n")

# seperating test and training data
dataAttributes = numpy.asarray (dataAttributes[1000:1050])

print ("Agglomerative Clustering Started")
linkage = "ward" # ward minimizes the variance of the clusters being merged
AggCluster = AgglomerativeClustering (linkage = linkage, n_clusters = 2).fit (dataAttributes)
print ("Agglomerative Clustering Finished\n")

pyplot.scatter (dataAttributes.T[0], dataAttributes.T[1], c = AggCluster.labels_)
pyplot.show ()