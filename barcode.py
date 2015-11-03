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
    seqDictCorrected = defaultdict(int)
    for b in barcodes:
        hamming_bnb_search(b, bcount, seqDictCorrected, args.maxdist)
    print bcount.values()
    return 0


def hamming_bnb_search(barcode, seqDict, seqDictCorrected, maxdist):
        minDist = maxdist
        best = None
        for seq in seqDict.keys():
            currDist = 0
            for a, b in zip(str(seq), barcode):
                currDist += (a != b)
                if currDist > minDist:
                    break
            if currDist < minDist:
                minDist = currDist
                best = seq
        if best is not None:
            seqDictCorrected[barcode] += seqDict[best]


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Barcode analysis.")
    parser.add_argument("-m", "--maxdist", action="store", type=int, default=4,
                        metavar="MAXDIST", dest="maxdist", help="Maximum Hamming distance for barcode match.")
    parser.add_argument("-b", "--barcode", action="store", type=str,
                        metavar="BARCODES", dest="bcfile", help="Path to barcode file.")
    parser.add_argument("fastq", nargs="?", metavar="FASTQ", help="Path to FASTQ file.")
    sys.exit(main(parser.parse_args()))
