def min_hamming(barcode, library, max_dist=2):

	if barcode in library:
		return barcode, 0

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

	return best_allele, min_dist
