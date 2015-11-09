import hamming
import pickle

with open('../../allele_dic_with_WT.pkl', 'rb') as f:
	library = pickle.load(f)

test_strings = [chr(x) * 18 for x in range(ord('A'), ord('Z'))]

for s in range(1, 4000):
	found, dist = hamming.calc_min_hamming('A' * 18, library)
