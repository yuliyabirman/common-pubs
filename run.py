import barcodes
import counts
#fastq_file_name, library_file_name, input_map_name, output_map_name,

indices = ['TTTCAC', 'GGCCAC', 'CGAAAC', 'CGTACG', 'CCACTC', 'GCTACC']


fastqs = []
for i in range(0, len(indices)):
	fastqs.append('../pynd_indices/pynd_' + str(i) + '_' + indices[i] + '.fastq')

empty_pkl = 'data/empty_pickle.pkl'
library = '../allele_dic_with_WT.pkl'

barcode_outputs = []
for i in range(0, len(indices)):
	barcode_outputs.append('../populations/barcode_' + str(i) + '_' + indices[i] + '.pkl')

freqs_outputs = []
for i in range(0, len(indices)):
	freqs_outputs.append('../populations/freqs_' + str(i) + '_' + indices[i] + '.pkl')

for i in range(0, len(indices)):
	print("Running barcode " + str(i))
	our_input = empty_pkl if i == 0 else barcode_outputs[i - 1]
	barcodes.update_read_map(fastqs[i], library, our_input, barcode_outputs[i])
	

for i in range(0, len(indices)):
	print("Running freqs " + str(i))
	counts.calc_mutant_freqs(fastqs[i], barcode_outputs[len(indices) - 1], library, freqs_outputs[i]) 
