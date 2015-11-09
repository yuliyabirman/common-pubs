import hamming

library = ['AABB', 'EEFF', 'ZYZY']

found, dist = hamming.calc_min_hamming('AAAA', library)
assert found == 'AABB'
assert dist == 2

found, dist = hamming.calc_min_hamming('QQQY', library)
assert found == None
assert dist == 4

found, dist = hamming.calc_min_hamming('EEFF', library)
assert found == 'EEFF'
assert dist == 0

found, dist = hamming.calc_min_hamming('AABC', library)
assert found == 'AABB'
assert dist == 1
