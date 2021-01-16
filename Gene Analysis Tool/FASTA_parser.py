def fasta_reader(file):
	mydict = {}

	with open(file) as f:
		for line in f:
			if line.startswith('>'):
				name = line.replace('\n', '')
				mydict[name] = ''
			else:
				mydict[name] += line.replace("\n", '')
	return mydict
