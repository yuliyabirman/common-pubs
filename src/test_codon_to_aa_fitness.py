import codon_to_aa_fitness as fitness

test = {(1, 'GTC'): 0.5, (5, 'GCC'): 0.6}

aas = fitness.convert(test)
assert (1, 'V') in aas
assert (5, 'A') in aas
assert aas[(1, 'V')] == 0.5
