import Orange
from Orange.regression import earth
import numpy
from matplotlib import pylab as pl
import sys
import matplotlib.dates as mdates

def get_data(f):
	d = []
	l = []
	count = 0
	for line in f:
		if count == 0:
			count = 1
			continue
		temp = line.strip().split(",")
		# print line
		# print line.strip().split(",")
		l.append(float(temp[-1]))
		d.append(temp[0])
	# print l
	return d,l

def get_lin_reg(x,y):
	data = Orange.data.Table("newdoc.csv")
	earth_predictor = earth.EarthLearner(data)

	tx1,ty1 = data.to_numpy("A/C")

	# pl.plot(x,y,".r")
	

	li = numpy.linspace(min(x), max(x), 20)
	# predictions = [earth_predictor([s, "?"]) for s in li]
	# pl.plot(linspace, predictions, "-b")
	# pl.show()
	data = Orange.data.Table("dat.tab")
	earth_predictor = earth.EarthLearner(data)

	X, Y = data.to_numpy("A/C")

	# pl.plot(X, Y, ".r")

	linspace = numpy.linspace(min(X), max(X), 20)
	predictions = [earth_predictor([s, "?"]) for s in linspace]

	# pl.plot(linspace, predictions, "-b")
	# pl.show()

	f = open("orangetrend.txt","w+")
	for i in range(len(linspace)):
		# print linspace
		# exit(0)
		f.write(str(linspace[i])+","+str(predictions[i])+"\n")

	f.close()

if __name__ == '__main__':
	f = open("newdoc.csv")
	dates,data = get_data(f)
	f.close()
	# print dates
	x = list(map(mdates.strpdate2num("%Y-%m-%d"),dates))
	# print x

	n = open("dat.tab","w+")
	n.write("X	Y\n")
	n.write("continuous	continuous \n \
	class\n")
	for i in range(len(x)):
		n.write(str(x[i])+"	" + str(data[i])+"\n")
	n.close()
	get_lin_reg(x,data)