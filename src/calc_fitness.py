import math
import sys
import pickle
import numpy
from scipy import stats
import os

homedir = os.path.expanduser('~')

def calc_ratio(frequencies):
  # find mutant positions
  # find WT positions
  # map residue positions to mutants and WT
  WT_frequency = None
  mutant_frequencies = {}
  for key, frequency in frequencies.items():
    codon = key[1]

    if codon == 'WT':
      assert WT_frequency == None
      WT_frequency = frequency
    else:
       mutant_frequencies[key] = frequency

  # calculate ratio
  #ratio = mutant_frequency / WT_frequency
  # calculate the ratio of each single-codon mutation relative to the wild-type sequence for each time point on a log2 scale
  return {key: numpy.log2(value / float(WT_frequency)) for key, value in mutant_frequencies.items()}

def load_ratios(pickle_file):
  with open(pickle_file, 'rb') as f:
    freqs = pickle.load(f)
    return calc_ratio(freqs)

def calc_regression(times, ratio_list):

  # get list of mutants to iterate over
  # this will be the union of the mutants across all of the time points
  mutants = set()
  for ratios in ratio_list:
    for mutant, ratios in ratios.items():
      mutants.add(mutant)

  slopes = {}

  # now calculate a regressino for each mutant
  for mutant in mutants:

    # get ratios with 0.0 for mutants that are not found
    new_ratios = []
    for ratios in ratio_list:
      if mutant in ratios:
        new_ratios.append(ratios[mutant])
      else:
        new_ratios.append(0)

    slope, intercept, r_value, p_value, std_err = stats.linregress(times, new_ratios)

    slopes[mutant] = slope

  return slopes

# TODO: Stop hardcoding
def main(args):

  test_name = args[1]
  
  # Day 1, timepoints T0, T1, T2
  # for each residue position, find log2 ratio for each time point
  # load input files containing the residue position, codon, and frequency

  ratios_0 = load_ratios(homedir + "/populations/pop0_" + test_name + "_0.pkl")
  ratios_1 = load_ratios(homedir + "/populations/pop1_" + test_name + "_1.pkl")
  ratios_2 = load_ratios(homedir + "/populations/pop2_" + test_name + "_2.pkl")
  ratios_3 = load_ratios(homedir + "/populations/pop3_" + test_name + "_3.pkl")
  ratios_4 = load_ratios(homedir + "/populations/pop4_" + test_name + "_4.pkl")
  ratios_5 = load_ratios(homedir + "/populations/pop5_" + test_name + "_5.pkl")

  times_day_1 = [0, 2.43, 4.11]
  times_day_2 = [0, 2.02, 4.16]

  fitness_day_1 = calc_regression(times_day_1, [ratios_0, ratios_1, ratios_2])
  fitness_day_2 = calc_regression(times_day_2, [ratios_3, ratios_4, ratios_5])

  pickle.dump(fitness_day_1, open(homedir + '/fitness/' + test_name + '_fitness_day_1', 'wb'))
  pickle.dump(fitness_day_2, open(homedir + '/fitness/' + test_name + '_fitness_day_2', 'wb'))

# determine selection coefficient, s,  for each mutation
# by finding the slope of this ratio to time in WT generations

if __name__ == '__main__':
  import sys
  main(sys.argv)
