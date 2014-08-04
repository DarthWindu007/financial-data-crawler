import sys

def datize(line):
	line_list = line.strip().split(",")
	date = line_list[0]
	data = list(map(float,line_list[1:]))
	return tuple([date]+data)
def extract_data(fname):
	f = open(fname)
	dic = {}
	count = 0
	for line in f:
		if len(line) <= 0 or line == "":
			continue
		if count == 0:
			dic["headers"] =  line.strip().split(",")
		else:
			dic[count] = datize(line)
		count+=1;
	return dic

if __name__ == '__main__':
	fname = sys.argv[1]
	data = extract_data(fname)
	print(data[1])