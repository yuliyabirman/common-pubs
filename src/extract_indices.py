import pt_hamming
#PyND_151103
#
#This works to create fastq files containing the sequences for each specified index from a fastq file
#containing sequences with multiple indices. - Paul, 15/11/03
#
#whangee_indicies = ['TTTCAC', 'GGCCAC', 'CGAAAC', 'CGTACG', 'CCACTC', 'GCTACC']
#pynd_indices = ['ATCAGT', 'GCTCAT', 'AGGAAT', 'CTTTTG', 'TAGTTG', 'CCGGTG']
control_indices = ['ATTCCG', 'AGCTAG', 'GTATAG']
indices = control_indices


def extract(input_file_name, output_file_prefix, max_hamming_dist = 0):

	output_files = []
	for i in range(0, len(indices)):
		output_files.append(open(output_file_prefix + str(i) + '_' + indices[i] + '.fastq', 'w'))

	with open(input_file_name, 'r') as input_file:
			
		n_saved = 0
		n_corrected = 0
		current_header=None
		current_sequence=None
		current_score=None
		i = 0
		for line in input_file:
			if i % 4 == 0:
				current_header = line
			elif i % 4 == 1:
				current_sequence = line
			elif i % 4 == 3:
				current_score = line
				try:
					index = current_header.split(':')[-1].strip()
					corrected_index, dist = pt_hamming.calc_min_hamming(index, indices, max_hamming_dist)
					if corrected_index is not None:
						n_saved += 1
						if dist > 0: n_corrected += 1
						index_pos = indices.index(corrected_index)
						output_file = output_files[index_pos]
						output_file.write(current_header)
						output_file.write(current_sequence)
						output_file.write('+\n')
						output_file.write(current_score)
				except:
					pass
			i += 1

	print(str(n_corrected) + " indices were corrected out of " + str(n_saved) + " saved.")

	for f in output_files:
		f.close()

def main(args):
	extract(args.fastq, args.indices, max_hamming=args.max_hamming)
		
if __name__ == '__main__':
        import sys
        import argparse
        parser = argparse.ArgumentParser("Extract reads with particular indices")
        parser.add_argument("-i", "--indices", required=True, nargs="+", action="store", type=str, default=None, dest="indices", help="List of indices to include. An output file will be generated for each output.")
        parser.add_argument("-f", "--fastq", action="store", type=str, dest="fastq", help="Input FastQ file.")
        parser.add_argument("-o", "--output-prefix", action="store", type=str, dest="output_prefix", help="Prefix path for output files. The remainder will be indexno._index_seq.fastq")
        parser.add_argument("-m", "--max-distance", action="store", type=int, dest="max", help="Maximum hamming distance to allow.")
        sys.exit(main(parser.parse_args()))
                                    

if __name__ == '__main__':
	import sys
	input_file_name = sys.argv[1]
	output_file_name = sys.argv[2]
	extract(input_file_name, output_file_name)
