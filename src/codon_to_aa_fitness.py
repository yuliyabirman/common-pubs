import pickle
from Bio.Seq import Seq
from Bio.Alphabet import generic_rna

def convert(codons):
	return {(key[0], str(Seq(key[1]).translate())): value for key, value in codons.items()}
	
