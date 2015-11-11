import pickle
import map_barcodes
import count_per_allele as counts
import time
import multiprocessing as mp
import os
import datetime

homedir = os.path.expanduser('~')

datadir = homedir + '/outputs/' + datetime.datetime.now().time().strftime('%Y-%m-%d_%H%M%S')
os.makedirs(datadir)

max_hamming_dist = 2

whangee_indicies = ['TTTCAC', 'GGCCAC', 'CGAAAC', 'CGTACG', 'CCACTC', 'GCTACC']
pynd_indices = ['ATCAGT', 'GCTCAT', 'AGGAAT', 'CTTTTG', 'TAGTTG', 'CCGGTG']
control_indices = ['ATTCCG', 'AGCTAG', 'GTATAG']

def run(indices):

	starting_barcode_map = datadir + '/populations/barcode_map_pyndexact_0_ATCAGT.pkl'
	library = homedir + '/allele_dic_with_WT.pkl'

	fastqs = []
	for i in range(0, len(indices)):
		fastqs.append(homedir + '/pynd_indices/pynd_' + str(i) + '_' + indices[i] + '.fastq')

	processes = []
	for i in range(0, len(indices)):
		print("Running map_barcodes " + str(i))
		process = mp.Process(target=map_barcodes.update_read_map, args=(fastqs[i], library, max_hamming_dist))
		processes.append(process)
		process.start()

	for process in processes:
		process.join()

	freqs_outputs = []
	for i in range(0, len(indices)):
		freqs_outputs.append(datadir + '/freqs_' + str(i) + '_' + indices[i] + '.pkl')

	for i in range(0, len(indices)):
		print("Running freqs " + str(i))
		result = counts.calc_mutant_freqs(fastqs[i], library, freqs_outputs[i]) 
		with open(freqs_outputs[i], 'wb') as f: pickle.dump(result, f)

def main(args):
	if args.control:
		run(control_indices)
	else:
		run(pynd_indices)

if __name__ == '__main__':
	import sys
	import argparse
	parser = argparse.ArgumentParser("Run whole pipeline")
	parser.add_argument("-c", "--control", action="store_true", dest="control", help="Run control instead of PYND")
	sys.exit(main(parser.parse_args()))

