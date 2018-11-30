#	Decision Tree Algorithm for Classification
#		Group 05 - ESD15I018, MFD15I014, CED15I031

""" Outline :  """

import numpy
import csv
import graphviz
from sklearn import tree

dataAttributes = []
dataClass = []

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

classNames = {}

entityIndex = [1,2,3,4,5,6,7,8,0]
attributesIndex = [1,2,3,4,5,6,7,8]
classIndex = 0

# Loading Data
print ("Data Loading Started"), 
with open ('../../Dataset/Generated Data Set/daily smoking times.csv') as csvdata: 
	readCSV = csv.reader (csvdata, delimiter=',')
	next (readCSV)	# Skipping Header content
	for row in readCSV: 
		for i in entityIndex: 
			if (row[i] in Attributes[str (i)]) == False: 
				Attributes[str (i)][row[i]] = len (Attributes[str (i)].keys())
				if (i == classIndex): 
					classNames[row[i]] = 0
		datarow = []
		try: 
			for i in attributesIndex: 
				datarow.append (Attributes[str (i)][row[i]])
			dataAttributes.append (datarow)
			dataClass.append (Attributes[str (classIndex)][row[classIndex]])
		except ValueError: 
			pass
feats = ["Age","TimeSlot(4-7)","TimeSlot(8-11)","TimeSlot(12-13)","TimeSlot(14-15)","TimeSlot(16-20)","TimeSlot(21-23)","TimeSlot(0-3)"]

print ("Features: ", feats)
print ("Class Labels: ", list (classNames.keys ()))

print ("Done Loading Data\n")

# seperating test and training data
testDataAttributes = numpy.asarray (dataAttributes [4500:])
checkDataClass = numpy.asarray (dataClass[4500:])
dataAttributes = numpy.asarray (dataAttributes[:4500])
dataClass = numpy.asarray (dataClass[:4500])

print ("Classifier training Started")
dTreeClf = tree.DecisionTreeClassifier()
dTreeClf = dTreeClf.fit (dataAttributes, dataClass)
print ("Classifier training Finished\n")

model_data = tree.export_graphviz (dTreeClf,
				out_file = "dTree.dot",
				feature_names = feats,
				class_names = list (classNames.keys ()),
				filled = True)

classPred = dTreeClf.predict (testDataAttributes)
totalPoints = float (testDataAttributes.shape[0])
mislabeled = float ((checkDataClass == classPred).sum())

print ("Number of mislabeled points out of total %d points : %d" % (totalPoints, mislabeled))
print ("Classifier Model Accuracy: ", (1 - (mislabeled / totalPoints)) * 100.0)

print ("convert dTree.dot to dTree.pdf using 'dot -Tpdf dTree.dot -o dTree.pdf'")

# checking with random record
randomIndex = 200
record = testDataAttributes[randomIndex]
print (record)
record = record.reshape (1, -1)
classPredSingle = dTreeClf.predict (record)
print ("Predicted Class Label: ")
print (classPredSingle)
print ("Actual Class Label : ")
print (checkDataClass[randomIndex])