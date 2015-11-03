import hamming
import parse

def barcodes(reads, alleles):
	"""
		reads: a FastQRecord iterator
	"""

	read_to_allele = {}
	allele_counts = {}
	for read in reads:
		read = read.sequence
		if read in read_to_allele:
			allele_counts[read_to_allele[allele]] += 1
		else:
			allele, hamming_dist = hamming.hamming(read, alleles)
			allele_counts[allele] += 1
			read_to_allele[read] = allele

	return allele_counts, set(reads) - set(read_to_allele.keys())

def calc_allele_counts(read_file, allele_pickle):
	import pickle
	barcodes(parse.parse(read_file), pickle.load(pickle_file)

if __name__ == 'main':
	import sys
	counts, unused = calc_allele_counts(sys.argv[1], sys.argv[2])
	with open(sys.argv[3], 'r') as f:
		for allele, count in counts.items():
			f.write(allele + ' = ' + str(count) + '\n')
		
