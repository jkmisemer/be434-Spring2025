#!/usr/bin/env python3
"""
Author : Julia <Add your email>
Date   : 2025-04-24
Purpose: Reverse compliment DNA
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Tetranucleotide Frequency",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("dna", metavar="DNA", help="A string of DNA or a file")

    args = parser.parse_args()

    if os.path.isfile(args.dna):
        args.dna = open(args.dna).read().rstrip()

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    dna = args.dna

    count = {}
    for base in dna:
        count[base] = count.get(base, 0) + 1

    list_of_counts = []
    for base in sorted(count):
        list_of_counts.append(count[base])
        # print(base, count[base])
    print(*list_of_counts)


# --------------------------------------------------
if __name__ == "__main__":
    main()
