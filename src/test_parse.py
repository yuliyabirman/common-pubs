import parse

records = list(parse.load_fastq('../test_resources/test_allele_shortrevcomp.fastq'))

assert len(records) == 6

assert records[0].sequence == 'ATATTGAAAGTATGCGCCAGATCGGA'
assert records[0].name == 'entry1'
