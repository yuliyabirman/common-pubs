from numba import jit

#@jit
def calc_min_hamming(barcode, library, max_dist = 2):
	"""
	library: a dictionary where the key is a barcode and the value is the tuple {position, codon}
	returns: a tuple (library_barcode, dist), where dist is the Hamming distance between barcode and library_barcode; if no matches are found, returns (None, max_dist)
	"""

	if barcode in library:
		return barcode, 0

	if max_dist == 0:
		return None, 0

	min_dist = len(barcode)
	best_barcode = None

	for allele in library:

		dist = 0

		for i in range(0, len(barcode)):
			if barcode[i] != allele[i]:
				dist += 1
				if dist > max_dist:
					dist = len(barcode)
					break
		if dist < min_dist:
			min_dist = dist
			best_allele = allele

		if min_dist == 1:
			return best_allele, min_dist 

	return best_allele if min_dist <= max_dist else None, min_dist
