#!/usr/bin/env python3
"""
Author : Julia Misemer
Date   : 2025-05-07
Purpose: Summarize sequence lengths from FASTA files
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Summarize FASTA file sequence lengths',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        nargs='+',
                        help='Input FASTA file(s)')

    return parser.parse_args()


# --------------------------------------------------
def read_fasta(filename):
    """Return list of sequence lengths"""

    lengths = []
    try:
        with open(filename) as fh:
            seq = ''
            for line in fh:
                line = line.strip()
                if line.startswith('>'):
                    if seq:
                        lengths.append(len(seq))
                        seq = ''
                else:
                    seq += line
            if seq:
                lengths.append(len(seq))
    except Exception as e:
        print(f"usage: {e}", file=sys.stderr)
        sys.exit(1)

    return lengths


# --------------------------------------------------
def main():
    """Main function"""

    args = get_args()

    # Print header
    print(f"{'name':<25} {'min_len':>8} {'max_len':>8} {'avg_len':>9} {'num_seqs':>10}")

    for filename in args.files:
        if not os.path.isfile(filename):
            print(f"usage: No such file or directory: '{filename}'", file=sys.stderr)
            sys.exit(1)

        lengths = read_fasta(filename)
        num = len(lengths)
        min_len = min(lengths) if lengths else 0
        max_len = max(lengths) if lengths else 0
        avg_len = (sum(lengths) / num) if num else 0.00

        # Output the result with proper formatting
        print(f"{filename:<25} {min_len:8} {max_len:8} {avg_len:9.2f} {num:10}")

        if num == 0:
            print(f"{filename}: No sequences found")
            sys.exit(1)
        else:
            print(f"{filename}: {num} sequences found")
            sys.exit(0)

# --------------------------------------------------
if __name__ == '__main__':
    main()
