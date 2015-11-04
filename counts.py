import pickle
import parse


def calc_mutant_freqs(fastq_records, read_to_mutant, library):
	counts = {}
	for read in fastq_records:
		read = read.get_barcode_rev_comp()
		mutant = read_to_mutant[read]
		if mutant not in counts:
			counts[mutant] = 0
		counts[mutant] += 1
	return counts
	#total = float(sum(counts.values))
	#return {value / total for value in counts}


if __name__ == '__main__':
	import sys
	fastq_records = parse.load_fastq(sys.argv[1])
	with open(sys.argv[2], 'rb') as f: read_to_mutant = pickle.load(f)
	with open(sys.argv[3], 'rb') as f: library = pickle.load(f)
	counts = calc_mutant_freqs(fastq_records, read_to_mutant, library)
	with open(sys.argv[4], 'wb') as f: pickle.dump(counts, f)
