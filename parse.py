class FastQRecord:

	barcode = None
	name = None
	quality = None

	def __init__(self, name, barcode, quality):
		self.barcode = barcode
		self.name = name
		self.quality = [ord(c) for c in list(quality)]


def parse(input_file_name):

        with open(input_file_name, 'r') as input_file:

                current_header=None
                current_sequence=None
                current_score=None
                i = 0
                for line in input_file:
                        if i % 4 == 0:
                                current_header = line
                        	i += 1
                        elif i % 4 == 1:
                                current_sequence = line
                        	i += 1
                        elif i % 4 == 3:
                                current_score = line
                        	i += 1
				name = current_header[1:].split()[0]
				yield FastQRecord(name, current_sequence, current_score)
				

