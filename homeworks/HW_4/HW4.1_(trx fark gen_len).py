file = "ensembl_hg19.txt"

def parse_to_exonC():
	exon_count = []
	with open(file) as file_handler:
		for line in file_handler:
			if line.startswith("#"):continue
			words = line.strip().split("\t")
			if words[4] == words[5]: continue
			exon_count.append(words[8])
	#print(exon_count)
	avg_exon_count = sum(map(int, exon_count))/len(exon_count)
	return int(avg_exon_count)
print("Average exon count is", parse_to_exonC())
def parse_to_Longestpos():
	gene_length = []
	gene = {}
	with open(file) as file_handler:
		for line in file_handler:
			if line.startswith("#"):continue
			words = line.strip().split("\t")
			if words[3] == "-": continue
			gene_name = words[12]
			gene_length.append((int(words[5])-int(words[4])))  #trx difference
			diff = int(words[5])-int(words[4])
			if gene_name not in gene:
				gene[gene_name] = diff
			#elif gene_name in gene and gene[gene_name] < diff:
			#	gene[gene_name].update(diff)
	longest = max(map(int, gene_length))
	for x,y in gene.items():
		if y == longest:
			longest_gene = x
			break
	return longest_gene, longest
print("+ Strand Longest:", parse_to_Longestpos())
def parse_to_Longestneg():
	gene_length = []
	gene = {}
	with open(file) as file_handler:
		for line in file_handler:
			if line.startswith("#"):continue
			words = line.strip().split("\t")
			if words[3] == "+": continue
			gene_length.append((int(words[5])-int(words[4])))
			diff = int(words[5]) - int(words[4])  # trx difference
			gene_name = words[12]
			if gene_name not in gene:
				gene[gene_name] = diff
			#elif gene_name in gene and gene[gene_name] < diff:
			#	gene[gene_name].update(diff)
		longest = max(map(int, gene_length))
		for x, y in gene.items():
			if y == longest:
				longest_gene = x
				break
	return longest_gene, longest
print("- Strand Longest:", parse_to_Longestneg())
def Avg_5UTR():
	Upstream = []
	Downstream = []
	with open(file) as filehandler:
		for line in filehandler:
			if line.startswith("#"): continue
			words = line.strip().split("\t")
			if words[3] == "+":						# strand <- word[3]
				UTR5 = int(words[6]) - int(words[4]) # cdsStart <- word[6], txStart <- word[4]
				Upstream.append(UTR5)
			elif words[3] == "-":
				UTR5 = int(words[5]) - int(words[7])  # cdsEnd <- word[7], txEnd <- word[5]
				Downstream.append(UTR5)
		#up_avg = sum(Upstream)/len(Upstream)
		#down_avg = sum(Downstream)/len(Downstream)
		Total = sum(Upstream)+ sum(Downstream)
		total_l = len(Upstream) + len(Downstream)
	return Total/total_l
print("Average 5_UTR:", Avg_5UTR())
def Avg_3UTR():
	Upstream = []
	Downstream = []
	with open(file) as filehandler:
		for line in filehandler:
			if line.startswith("#"): continue
			words = line.strip().split("\t")
			if words[3] == "+":						# strand <- word[3]
				UTR3 = int(words[5]) - int(words[7]) # cdsStart <- word[6], txStart <- word[4]
				Upstream.append(UTR3)
			elif words[3] == "-":
				UTR3 = int(words[6]) - int(words[4])  # cdsEnd <- word[7], txEnd <- word[5]
				Downstream.append(UTR3)
		#up_avg = sum(Upstream)/len(Upstream)
		#down_avg = sum(Downstream)/len(Downstream)
		Total = sum(Upstream)+ sum(Downstream)
		total_l = len(Upstream) + len(Downstream)
	return Total/total_l
print("Average 3_ UTR:", Avg_3UTR())