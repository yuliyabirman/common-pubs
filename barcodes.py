import hamming
import parse
import pickle
from Bio.Seq import Seq

#PyND_151103

def update_read_map(fastq_file_name, library_file_name, input_map_name, output_map_name, max_hamming_dist = 2):
	with open(input_map_name, 'rb') as f: input_map = pickle.load(f)
	with open(library_file_name, 'rb') as f: library = pickle.load(f)
	fastq_records = parse.load_fastq(fastq_file_name)
	new_map = guess_alleles(fastq_records, library, input_map, max_hamming_dist = max_hamming_dist)
	with open(output_map_name, 'wb') as f: pickle.dump(new_map, f)
	

def guess_alleles(fastq_records, library, read_to_allele, max_hamming_dist = 2):
	n_unmatched = 0
	for read in fastq_records:
		if read not in read_to_allele:
			rev_comp =  str(Seq(str(read.sequence)[:-8]).reverse_complement())
			allele, hamming_dist = hamming.calc_min_hamming(rev_comp, library, max_hamming_dist)
			if allele is None:
				n_unmatched += 1
			else:
				read_to_allele[rev_comp] = allele
			#try:
			#	read_to_allele[rev_comp] = library[rev_comp]
			#except KeyError:
			#	n_unmatched += 1
	print("There were %i unmatched reads." % n_unmatched)
	return read_to_allele
	

def main(args):
	update_read_map(args.fastq, args.library, args.inp, args.output, max_hamming_dist = args.max)

if __name__ == '__main__':
	import sys
	import argparse
	parser = argparse.ArgumentParser("Map read sequences to known barcodes.")
	parser.add_argument("-l", "--library", action="store", type=str, default=None, dest="library", help="Pickle with barcode definitions.")
	parser.add_argument("-f", "--fastq", action="store", type=str, dest="fastq", help="Input FastQ file.")
	parser.add_argument("-i", "--input", action="store", type=str, dest="inp", help="Output pickle of a dictionary mapping read sequences to known alleles.")
	parser.add_argument("-o", "--output", action="store", type=str, dest="output", help="Output pickle of a dictionary mapping read sequences to known alleles.")
	parser.add_argument("-m", "--max-distance", action="store", type=int, dest="max", help="Maximum hamming distance to allow.")
	sys.exit(main(parser.parse_args()))
