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


def complement_seq(seq_input):
	#Returns complementary sequence 3' --> 5'
	comp_seq = []
	sequence = seq_input.upper()

	for letter in sequence:
		if letter == "A":
			comp_seq.append("T")
		elif letter == "T":
			comp_seq.append("A")
		elif letter == "G":
			comp_seq.append("C")
		elif letter == "C":
			comp_seq.append("G")
		elif letter == 'N':
			comp_seq.append("G")
	comp_seq.reverse()
	c_seq = "".join(comp_seq)

	return c_seq


def transcription(sequence):
	seq = ''
	dna_seq = 'ATGC'

	for letter in sequence.upper():
		if letter not in dna_seq:
			raise Exception(f'{letter} is not a DNA nucleotide')
		if letter == "T":
			seq += "U"
		else:
			seq += letter

	return seq


def reverse_transcription(rna_sequence):
	seq = ''
	rna_seq = 'AUGC'
	for letter in rna_sequence.upper:
		if letter not in rna_seq:
			raise Exception(f'{letter} is not a RNA nucleotide')
		if letter == "U":
			seq += "T"
		else:
			seq += letter

	return seq


def translate(dna_seq):


	rv = ''
	table = {
		'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
		'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
		'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
		'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
		'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
		'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
		'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
		'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
		'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
		'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
		'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
		'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
		'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
		'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
		'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
		'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
	}

	for idx in range(int(len(dna_seq)/3)):
		codon = dna_seq[idx*3:idx*3+3]

		if table[codon] == '_':
			break
		rv += table[codon]

	return rv


def atgc_counter(dna_seq):
	A_counter = 0
	T_counter = 0
	G_counter = 0
	C_counter = 0
	nan_dna = 0
	sequence = dna_seq.upper()

	for letter in sequence:
		if letter == "A":
			A_counter += 1
		elif letter == "T":
			T_counter += 1
		elif letter == "G":
			G_counter += 1
		elif letter == "C":
			C_counter += 1
		else:
			nan_dna += 1

	return f'A: {A_counter}\t T: {T_counter}\t G:{G_counter}\t C:{C_counter}\t others:{nan_dna}'


def gc_contenter(seq):
	c = 0
	for letter in seq:
		if letter == "G" or letter == "C":
			c += 1
	rv = c/len(seq)

	return round(rv*100,5)


def protein_mass(protein_seq):

	pro_seq = protein_seq.upper()
	weight_dict = {
		'A':71.03711,
		'C': 103.00919,
		"D":115.02694,
		"E":129.04259,
		"F":147.06841,
		"G":57.02146,
		"H":137.05891,
		"I":113.08406,
		"K":128.09496,
		"L":113.08406,
		"M": 131.04049,
		"N":114.04293,
		"P":97.05276,
		"Q":128.05858,
		"R":156.10111,
		"S":87.03203,
		"T":101.04768,
		"V":99.06841,
		"W":186.07931,
		"Y":163.06333
	}
	weight_sum = 0

	for seq in pro_seq:
		if seq in weight_dict:
			weight_sum += weight_dict[seq]
		else:
			raise Exception(f'{seq} is not a valid amino acid')

	return weight_sum.__round__(3)


def motif_finder(motif, sequence):
	#Returns a list
	aa = []
	seq = sequence

	for position, letter in enumerate(seq):

		if motif == seq[position:position +len(motif)]:
			aa.append(position+1)

	return aa


def consensus(seq_list):
	'''
    :param seq_list:  takes list of dna sequences
    :return: consensus sequence in string format
    '''
	sequences = seq_list

	a = []
	t = []
	g = []
	c = []

	for position, letter in enumerate(sequences[0]):
		A_counter = 0
		T_counter = 0
		G_counter = 0
		C_counter = 0
		for index in range(len(sequences)):
			if sequences[index][position] == "A": A_counter += 1
			if sequences[index][position] == "T": T_counter += 1
			if sequences[index][position] == "G": G_counter += 1
			if sequences[index][position] == "C": C_counter += 1
		a.append(A_counter)
		t.append(T_counter)
		g.append(G_counter)
		c.append(C_counter)

	consensus_seq = []

	for p, v in enumerate(a):
		consensus_max = max(v, c[p], g[p], t[p])
		if consensus_max == a[p]:
			consensus_seq.append("A")

		if consensus_max == c[p]:
			consensus_seq.append("C")

		if consensus_max == g[p]:
			consensus_seq.append("G")

		if consensus_max == t[p]:
			consensus_seq.append("T")

	consensus_seq_str = ''.join(consensus_seq)
	return consensus_seq_str