import fitness

times = [1.0, 2.0, 3.0]
ratios = [{(1, 'A'): 0.4}, {(1, 'A'): 0.5}, {(1, 'A'): 0.6, (0, 'WT'): 0.7}]
fitnesses = fitness.calc_regression(times, ratios)
assert len(fitnesses) == 2
assert (1, 'A') in fitnesses
assert abs(fitnesses[(1, 'A')] - 0.1) < 0.000001
assert (0, 'WT') in fitnesses
assert abs(fitnesses[(0, 'WT')] - 0.35) < 0.0000001
