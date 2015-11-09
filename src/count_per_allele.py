import pickle
import parse
#PyND_151104pt

dict_prefix = 'lib:pynd_'


def calc_mutant_freqs(fastq_records, red, library):
	counts = {}
	for read in fastq_records:
		read = read.get_barcode_rev_comp()
		if dict_prefix + read in red:
			mutant = read_to_mutant[read]
			if mutant not in counts:
				counts[mutant] = 0
			counts[mutant] += 1
	total = float(sum(counts.values()))
	freqs = {}
	for key, value in counts.items():
		freqs[key] = value / total
	return freqs


def main(args):
	red = redis.StrictRedis(host='localhost')
	calc_mutant_freqs(parse.load_fastq(args.fastq), red, args.library)
	counts = calc_mutant_freqs(args.fastq_records, args.library)
	with open(args.output, 'wb') as f: pickle.dump(counts, f)

if __name__ == '__main__':
        import sys
        import argparse
        parser = argparse.ArgumentParser("Count the number of reads that mapped to each mutant.")
        parser.add_argument("-l", "--library", action="store", type=str, default=None, dest="library", help="Pickle with barcode definitions.", required=True)
        #parser.add_argument("-f", "--fastq", action="store", type=str, dest="fastq", help="Input FastQ file.")
        #parser.add_argument("-i", "--input", action="store", type=str, dest="inp", help="Output pickle of a dictionary mapping read sequences to known alleles.")
        parser.add_argument("-o", "--output", action="store", type=str, dest="output", help="Output pickle of a dictionary mapping mutants in the form (position, codon) to their frequencies in reads.", required=True)
        sys.exit(main(parser.parse_args()))
