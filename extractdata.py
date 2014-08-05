import sys

def datize(line):
	"""
	Converting a line into a tuple in the format 
	of (str,float,float,float,float,float,float)
	"""
	line_list = line.strip().split(",")
	date = line_list[0].split("-")
	date = "/".join(date[1:]+[date[0]])
	data = list(map(float,line_list[1:]))
	return tuple([date]+data)
def extract_data(fname):
	"""
	Takes a file and returns a list of data.
	Assuming it is correctly formated, the headers
	can be found by accessing dic[0].
	"""
	f = open(fname)
	dic = []
	count = 0
	for line in f:
		if len(line) <= 0 or line == "":
			continue
		if count == 0:
			s = line.strip().split(",")
			dic.append(s)
		else:
			dic.append(datize(line))
		count+=1;
	return dic

if __name__ == '__main__':
	# This is just for testing purposes mainly, probably won't call this function
	fname = sys.argv[1]
	data = extract_data(fname)
	print(data)