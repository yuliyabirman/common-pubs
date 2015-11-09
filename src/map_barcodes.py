import hamming
import parse
import pickle
from Bio.Seq import Seq
import redis
from random import shuffle

#PyND_151103

dict_prefix = 'lib:pynd_'

def update_read_map(fastq_file_name, library_file_name, max_hamming_dist = 2, shuffle=False):
	red = redis.StrictRedis(host='localhost')
	#with open(input_map_name, 'rb') as f: input_map = pickle.load(f)
	with open(library_file_name, 'rb') as f: library = pickle.load(f)
	fastq_records = parse.load_fastq(fastq_file_name)
	if (shuffle):
		fastq_records = shuffle(list(fastq_records))
	guess_alleles(fastq_records, library, red, max_hamming_dist = max_hamming_dist)
	#with open(output_map_name, 'wb') as f: pickle.dump(new_map, f)
	

def guess_alleles(fastq_records, library, redis_db, max_hamming_dist = 2):
	n_unmatched = 0
	for read in fastq_records:
		rev_comp = read.get_barcode_rev_comp() 
		got = red.get(dict_prefix + rev_comp)
		#if read not in read_to_allele:
		if got is not None:
			allele, hamming_dist = hamming.calc_min_hamming(rev_comp, library, max_hamming_dist)
			# TODO: don't try hamming correction if it's another group's
			if allele is None:
				n_unmatched += 1
			else:
				redis.set(dict_prefix + rev_comp, allele)
				#read_to_allele[rev_comp] = allele
			#try:
			#	read_to_allele[rev_comp] = library[rev_comp]
			#except KeyError:
			#	n_unmatched += 1
	print("There were %i unmatched reads." % n_unmatched)
	#return read_to_allele
	

def main(args):
	update_read_map(args.fastq, args.library, args.inp, args.output, max_hamming_dist = args.max_hamming, shuffle = args.shuffle)

if __name__ == '__main__':
	import sys
	import argparse
	parser = argparse.ArgumentParser("Map read sequences to known barcodes.")
	parser.add_argument("-l", "--library", action="store", type=str, default=None, dest="library", help="Pickle with barcode definitions.")
	parser.add_argument("-f", "--fastq", action="store", type=str, dest="fastq", help="Input FastQ file.")
	#parser.add_argument("-i", "--input", action="store", type=str, dest="inp", help="Output pickle of a dictionary mapping read sequences to known alleles.")
	#parser.add_argument("-o", "--output", action="store", type=str, dest="output", help="Output pickle of a dictionary mapping read sequences to known alleles.")
	parser.add_argument("-m", "--max-distance", action="store", type=int, dest="max_hamming", help="Maximum hamming distance to allow.")
	parser.add_argument("-s", "--shuffle", action="store_true", dest="shuffle", help="Shuffle the FastQ input. Useful when running multiple processes for a single file.")
	sys.exit(main(parser.parse_args()))
