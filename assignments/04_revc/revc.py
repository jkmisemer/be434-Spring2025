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
        description="Reverse compliment DNA",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "dna", metavar="DNA", help="Print the reverse complement of DNA"
    )

    args = parser.parse_args()

    if os.path.isfile(args.dna):
        args.dna = open(args.dna).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    dna = args.dna

    complement = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C",
        "a": "t",
        "t": "a",
        "c": "g",
        "g": "c",
    }
    revc = []
    for base in dna:
        revc.append(complement[base])
    print("".join(revc[::-1]))


# --------------------------------------------------
if __name__ == "__main__":
    main()
