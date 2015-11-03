#!/usr/bin/env python2.7
import sys
import os
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from collections import defaultdict
from Bio import SeqIO


def main(args):
    with open(args.bcfile, 'rU') as f:
        barcodes = [l.rstrip(os.linesep) for l in f]
    bcount = defaultdict(int)
    with open(args.fastq, 'rU') as f:
        for record in SeqIO.parse(f, 'fastq'):
            s = record.seq.reverse_complement()[::-1]
            q = record.letter_annotations['phred_quality']
            bcount[s[0:18]] += 1
    # for b in barcodes:
    #     print b + '\t' + str(bcount[b])
    print bcount.values()
    return 0


seqDict = defaultdict(int)
seqDictCorrected = defaultdict(int)


def hamming_bnb_search(barcode_dic, seqDict):
    for barcode in barcode_dic:
        minDist = 4
        for seq in seqDict.keys():
            currDist = 0
            for a, b in zip(str(seq), barcode):
                currDist += (a != b)
                if currDist > minDist:
                    break
            if currDist < minDist:
                minDist = currDist
                seqDictCorrected[barcode] += seqDict[seq]


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Barcode analysis.")
    parser.add_argument("-b", "--barcode", action="store", type=str,
                        metavar="BARCODES", dest="bcfile", help="Path to barcode file.")
    parser.add_argument("fastq", nargs="?", metavar="FASTQ", help="Path to FASTQ file.")
    sys.exit(main(parser.parse_args()))
