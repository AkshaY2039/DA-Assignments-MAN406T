#	K-Means Algorithm for Clustering
#		Group 05 - ESD15I018, MFD15I014, CED15I031

""" Outline :  """

import numpy
import csv
from matplotlib import pyplot
from sklearn.cluster import KMeans

dataAttributes = []

Attributes = {
	"0": {},	# Gender
	"1": {},	# age
	"2": {},	# Number of cigarettes per day
}

# age and Number of cigarettes per day
entityIndex = [1,2]

# Loading Data
print ("Data Loading Started"), 
with open ('../../Dataset/Generated Data Set/number of cigarettes per day.csv') as csvdata: 
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
feats = ["Age","Number of Cigarettes per Day"]

print ("Features: ", feats)

print ("Done Loading Data\n")

# seperating test and training data
testDataAttributes = numpy.asarray (dataAttributes[11000:])
dataAttributes = numpy.asarray (dataAttributes[:11000])

print ("KMeans Clustering Started")
KMCluster = KMeans (n_clusters = 3, random_state = 0).fit (dataAttributes)
predCluster = KMCluster.predict (testDataAttributes)
print ("KMeans Clustering Finished\n")

# adding 10 as the first key it will take to b 0
pyplot.scatter (testDataAttributes.T[0] + 10, testDataAttributes.T[1], c = predCluster)
pyplot.show ()