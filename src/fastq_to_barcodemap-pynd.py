import pickle
#import barcodes
import map_barcodes
import counts
#PyND_151104

homedir = os.path.expanduser('~')

#fastq_file_name, library_file_name, input_map_name, output_map_name,
whangee_indicies = ['TTTCAC', 'GGCCAC', 'CGAAAC', 'CGTACG', 'CCACTC', 'GCTACC']
pynd_indices = ['ATCAGT', 'GCTCAT', 'AGGAAT', 'CTTTTG', 'TAGTTG', 'CCGGTG']
control_indices = ['ATTCCG', 'AGCTAG', 'GTATAG']


indices = pynd_indices
starting_barcode_map = homedir + '/populations/barcode_map_pyndexact_0_ATCAGT.pkl'
library = homedir + '/allele_dic_with_WT.pkl'
max_hamming_dist = 2

fastqs = []
for i in range(0, len(indices)):
	fastqs.append(homedir + '/pynd_indices/pynd_' + str(i) + '_' + indices[i] + '.fastq')


map_barcodes_outputs = []
for i in range(0, len(indices)):
	map_barcodes_outputs.append(homedir + '/populations/barcode_map_pyndham2_' + str(i) + '_' + indices[i] + '.pkl')

#freqs_outputs = []
#for i in range(0, len(indices)):
#	freqs_outputs.append('~/populations/freqs_' + str(i) + '_' + indices[i] + '.pkl')

for i in range(0, len(indices)):
	#print("Running map_barcodes " + str(i))
	input_map = starting_barcode_map if i == 0 else map_barcodes_outputs[i - 1]
	map_barcodes.update_read_map(fastqs[i], library, input_map, map_barcodes_outputs[i], max_hamming_dist)
	print("Running map_barcodes " + str(i))

#for i in range(0, len(indices)):
#	print("Running freqs " + str(i))
#	result = counts.calc_mutant_freqs(fastqs[i], barcode_outputs[len(indices) - 1], library, freqs_outputs[i]) 
#	with open(freqs_outputs[i], 'wb') as f: pickle.dump(result, f)
