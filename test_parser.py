import parser

parser.extract('test.fastq', 'output_test.fastq', 5, frozenset(['header1', 'header3']))

with open('output_test.fastq') as f:
	lines = list(f.readlines())
	text = ''.join(lines)
	print(text)
	print(type(text))
	assert 'header1' in text
	assert 'header2' not in text
	assert 'header3' not in text
