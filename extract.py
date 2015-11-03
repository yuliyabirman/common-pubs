indicies = ['TTTCAC', 'GGCCAC', 'CGAAAC', 'CGTACG', 'CCACTC', 'GCTACC']

#def read_indicies(file_name):
#	with open(file_name) as f:
#		return frozenset(list(f.readlines()))

def extract(input_file_name, output_file_prefix):

	output_files = []
	for i in range(0, len(indicies)):
		output_files.append(open(output_file_prefix + str(i) + '_' + indicies[i] + '.fastq', 'w'))

	with open(input_file_name, 'r') as input_file:
			
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
					index_pos = indicies.index(current_header.split(':')[-1].strip())
					output_file = output_files[index_pos]
					output_file.write(current_header)
					output_file.write(current_sequence)
					output_file.write('+\n')
					output_file.write(current_score)
				except:
					pass
			i += 1

	for f in output_files:
		f.close()
		

if __name__ == '__main__':
	import sys
	input_file_name = sys.argv[1]
	output_file_name = sys.argv[2]
	min_qual_score = int(sys.argv[3])
	#indicies = read_indicies(sys.argv[4])
	extract(input_file_name, output_file_name)
