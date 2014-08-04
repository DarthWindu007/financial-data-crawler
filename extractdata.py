import sys

def datize(line):
	"""
	Converting a line into a tuple in the format 
	of (str,float,float,float,float,float,float)
	"""
	line_list = line.strip().split(",")
	date = line_list[0]
	data = list(map(float,line_list[1:]))
	return tuple([date]+data)
def extract_data(fname):
	"""
	Takes a file and returns a dictionary of data.
	Assuming it is correctly formated, the headers
	can be found by accessing dic["headers"] or dic[0].
	"""
	f = open(fname)
	dic = {}
	count = 0
	for line in f:
		if len(line) <= 0 or line == "":
			continue
		if count == 0:
			s = line.strip().split(",")
			dic["headers"] = s
			dic[0] = s
		else:
			dic[count] = datize(line)
		count+=1;
	return dic

if __name__ == '__main__':
	fname = sys.argv[1]
	data = extract_data(fname)
	print(data[1])