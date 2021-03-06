sequence = "GTGTGTTTAGTCCGCCCACGTGTAATTCGTGCGTAGTGCTTTCTTGGTATCTTCCGTATGTCCCCCGCGTTGCTGTCCTTTGCCTTTGAACGTCCACCTATGCTGTGGGGGAGCTCAACTATGCTTCGTCATATGGTCTGTTCATGCTCATAAAGGGGATCTGTCGCCTAGCATAGGCAATAGCGAGTAGGGCCCTTTATAACGCCCAATTAATGTGGCGCATGCGCTCTGACACGAACATACCGCGAACCCTTCATGGCGCCCTCTTAGACTTATTGGACGAGCCCAACGGGCCGGAAGCGATTCCGAAACGGGAAGGTGGCCAGGCCTGGGTGCATTTCTTTACCTAATACATATCGCGACTCATCGGTCGATAAGGCCTCCGGTTACATCCTGTATCGCCATCAAAGTAACCACGTTGGGGCCTTATAGACGACGAGTCTCTGCGAGGGCCCTAAACTTGTGATAAGGATGAGGTATTAGGTTAAACGCTGATGAGCGTATCCCTAGGGCAAGAAGCCACCAAGCCACCCAATTGCTGTCTGAGTGCACTGACATGACATGTAACGTTCATATAGGCGTAATTCAGTAGGACGTGGCCGGGGGATGGTGGACCGAAGCCTTCTGGAACGCGGATACATTTTATCACTGACCCATCTTCTGTTTCATTCGACCAGCAGCTCCTGACTAATGGTAGGAATATGTTGCTCCTCGGCAGTACTTCCGTGAGGGATCCGCGTCACGCACGGCCCATTAGGGGTCATGCCTTTAGCCAAGAGGATTGGATTCTCACGAGGGCAT"

def ATCG_counter(dna_seq):
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

print(ATCG_counter(sequence))