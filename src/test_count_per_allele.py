import count_per_allele as count
import parse
from parse import FastQRecord
import unittest
import unittest.mock
from unittest.mock import patch
import logging

prefix = 'lib:pynd_'
class Red:

	data = None

	def __init__(self):
		self.data = {}
	def set(self, key, val):
		self.data[key] = val
	def get(self, key):
		return self.data[key]
	def __contains__(self, key):
		return self.data[key] != None

class TestIt(unittest.TestCase):

	def return_self(*args):
		return args[0]

	#@patch('redis.StrictRedis.get')
	#@patch('redis.StrictRedis.set')
	@patch('parse.FastQRecord', 'get_barcode_rev_comp')
	def test(self, rev_comp):
		print("Running")
		#rev_comp.side_effect = lambda s: s
		#records = list(parse.load_fastq('../test_resources/test_allele_shortrevcomp.fastq'))
		records = []
		records.extend([FastQRecord('a', 'a', ''), FastQRecord('a', 'a', ''), FastQRecord('a', 'a', ''), FastQRecord('b', 'b', ''), FastQRecord('b', 'b', ''), FastQRecord('c', 'c', '')])
		library = ['A', 'B', 'C']
		red = Red()
		red.data = {'a': 'A', 'aa': 'A', 'aaa': 'A', 'b': 'B', 'bb': 'B', 'c': 'C'}
		red.data = {lambda key, val: key: prefix + val for key, val in red.data.items()}

		#read_count = 0
		def side_effect(self):
			log.debug(self.sequence)
			return self.sequence
			#read_count += 1
			#return records[read_count - 1].sequence

		#rev_comp.side_effect = lambda self: self.sequence
		#rev_comp.side_effect = side_effect
		freqs = count.calc_mutant_freqs(records, red, library)
		print(freqs)


if __name__ == '__main__':
	unittest.main(lambda self: self.sequence)
