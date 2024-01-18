import requests

#HW6.2
def fetch_sequence_fromtogows(chrom, start, end, genomeversion='hg19'):
	url = f"http://togows.org/api/ucsc/{genomeversion}/chr{chrom.lower().replace('chr', '')}:{start}-{end}"
	return requests.get(url).content.decode()


def comp_seq(seq_input):
	comp_seq = []

	for letter in seq_input:

		if letter == "A":
			comp_seq.append("T")
		elif letter == "T":
			comp_seq.append("A")
		elif letter == "G":
			comp_seq.append("C")
		elif letter == "C":
			comp_seq.append("G")

	comp_seq.reverse()
	c_seq = "".join(comp_seq)

	return c_seq


class transcript():
	def __init__(self, id, ts_start, ts_end, strand, chrom):
		self.id = id
		self.chrom = chrom
		self.strand = strand
		self.ts_start = int(ts_start)
		self.ts_end = int(ts_end)

	def promoter_seq(self):

		if self.strand == "+":
			my_prom_end = self.ts_start
			my_prom_start = my_prom_end - 5000
			promoter = fetch_sequence_fromtogows(self.chrom, my_prom_start, my_prom_end)

		elif self.strand == "-":
			my_prom_end = self.ts_end
			my_prom_start = my_prom_end + 5000
			promoter = fetch_sequence_fromtogows(self.chrom, my_prom_end, my_prom_start)
			promoter = comp_seq(promoter)

		return promoter


def parse(text):
	# To parse ensenmbl dataframe only for chr 22
	with open(text) as sequence:
		dic = {}
		for line in sequence:
			if line.startswith("#"): continue

			boluk = line.strip().split()
			id = boluk[1]
			ts_start = boluk[4]
			ts_end = boluk[5]
			# cds_start=boluk[6]
			# cds_end=boluk[7]
			strand = boluk[3]
			chrom = boluk[2]

			if chrom == "chr22":
				dic[id] = transcript(id, ts_start, ts_end, strand, chrom)

	return dic


pfile = "Promoter_seqs(5000).txt"
parsed_dic = parse("Assignments/ensembl_hg19.txt")

with open(pfile, "w") as fh:
	fh.write("Tx_id\tchr\tstrand\tpromoter_sequence\n")
	for tf in parsed_dic:
		fh.write(
			f"{parsed_dic[tf].id}\t{parsed_dic[tf].chrom}\t{parsed_dic[tf].strand}\t{parsed_dic[tf].promoter_seq()}\n")
